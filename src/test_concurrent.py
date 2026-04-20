"""测试：Python 标准并发/异步模块的基本用法（pytest 风格）"""
import threading
import time as _time
import asyncio
import sys
import pytest
from concurrent.futures import ThreadPoolExecutor


def test_threading_basic():
    """TestThreadingBasic：创建线程、启动、 join、当前线程信息"""
    results = []
    def worker():
        results.append(1)
    t = threading.Thread(target=worker, name="Worker-1")
    t.start()
    t.join(timeout=1)
    assert t.is_alive() is False
    assert results == [1]
    assert threading.current_thread().name == "MainThread"


def test_thread_class():
    """TestThreadClass：自定义 Thread 子类"""
    results = []
    class MyThread(threading.Thread):
        def __init__(self, out, val):
            super().__init__()
            self.out = out
            self.val = val
        def run(self):
            self.out.append(self.val)
    t = MyThread(results, 5)
    t.start()
    t.join()
    assert results == [5]


def test_lock_and_rlock():
    """TestLock 与 TestRLock：互斥与可重入锁"""
    lock = threading.Lock()
    shared = {"n": 0}
    def worker():
        for _ in range(1000):
            with lock:
                shared["n"] += 1
    t1 = threading.Thread(target=worker)
    t2 = threading.Thread(target=worker)
    t1.start(); t2.start(); t1.join(); t2.join()
    assert shared["n"] == 2000

    rlock = threading.RLock()
    value = {"n": 0}
    def nested():
        with rlock:
            value["n"] += 1
            with rlock:
                value["n"] += 1
    t = threading.Thread(target=nested)
    t.start(); t.join()
    assert value["n"] == 2


def test_semaphore_and_event():
    """TestSemaphore 与 TestEvent：信号量和事件"""
    sem = threading.Semaphore(2)
    active = {"n": 0, "peak": 0}
    results = []
    def worker():
        with sem:
            active["n"] += 1
            if active["n"] > active["peak"]:
                active["peak"] = active["n"]
            _time.sleep(0.01)
            active["n"] -= 1
            results.append(1)
    threads = [threading.Thread(target=worker) for _ in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert sum(results) == 3
    assert active["peak"] <= 2

    ev = threading.Event()
    flag = []
    def waiter():
        ev.wait()
        flag.append(True)
    t = threading.Thread(target=waiter)
    t.start()
    _time.sleep(0.01)
    ev.set()
    t.join()
    assert flag == [True]


def test_condition_basic():
    cond = threading.Condition()
    ready = {"val": False}
    def waiter():
        with cond:
            while not ready["val"]:
                cond.wait()
            # 条件满足，继续执行
    def setter():
        with cond:
            ready["val"] = True
            cond.notify_all()
    w = threading.Thread(target=waiter)
    s = threading.Thread(target=setter)
    w.start(); _time.sleep(0.01); s.start(); w.join(); s.join()
    assert ready["val"] is True


def test_thread_pool_executor():
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(lambda x: x + 1, i) for i in range(3)]
        results = [f.result() for f in futures]
    assert results == [1, 2, 3]
    with ThreadPoolExecutor(max_workers=2) as executor:
        results_map = list(executor.map(lambda x: x * 2, [1, 2, 3]))
    assert results_map == [2, 4, 6]


pytestmark_none = None  # used to satisfy static analyzers in some environments


# 下面的测试对多进程/异步的测试在 Windows 上可能受限，若在具体环境需要可启用。
@pytest.mark.skipif(sys.platform.startswith("win"), reason="在 Windows 上多进程测试可能需要额外保护")
def test_multiprocessing_basic():  # pragma: no cover
    from multiprocessing import Process, Queue
    def worker(q, x):
        q.put(x * x)
    q = Queue()
    p = Process(target=worker, args=(q, 3))
    p.start()
    p.join(timeout=5)
    assert q.get() == 9


@pytest.mark.skipif(sys.platform.startswith("win"), reason="在 Windows 上多进程测试可能需要额外保护")
def test_process_pool_basic():  # pragma: no cover
    from concurrent.futures import ProcessPoolExecutor
    def f(x):
        return x * x
    with ProcessPoolExecutor(max_workers=2) as ex:
        res = list(ex.map(f, [2, 3]))
    assert res == [4, 9]


def test_asyncio_basic():
    """asyncio基本用法：async def, await, asyncio.run"""
    async def coro():
        await asyncio.sleep(0)
        return 123
    res = asyncio.run(coro())
    assert res == 123


def test_async_context_manager():
    """异步上下文管理器"""
    class AsyncCM:
        async def __aenter__(self):
            return 1
        async def __aexit__(self, exc_type, exc, tb):
            return False
    async def _run():
        async with AsyncCM() as v:
            assert v == 1
    asyncio.run(_run())


def test_async_generator():
    """异步生成器"""
    async def agen():
        for i in range(3):
            yield i
    async def collect():
        vals = []
        async for v in agen():
            vals.append(v)
        return vals
    vals = asyncio.run(collect())
    assert vals == [0, 1, 2]
