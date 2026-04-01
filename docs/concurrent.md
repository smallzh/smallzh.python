# 并发编程

Python 提供了多种并发编程方式：多线程、多进程和异步编程。

## 0x01. 多线程

### 基本使用

```python
import threading
import time

def worker(name, delay):
    """工作线程函数"""
    print(f'线程 {name} 开始')
    time.sleep(delay)
    print(f'线程 {name} 结束')

# 创建线程
t1 = threading.Thread(target=worker, args=('A', 2))
t2 = threading.Thread(target=worker, args=('B', 1))

# 启动线程
t1.start()
t2.start()

# 等待线程完成
t1.join()
t2.join()

print('所有线程完成')
```

### Thread 类

```python
import threading

# 继承 Thread 类
class MyThread(threading.Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay
    
    def run(self):
        print(f'线程 {self.name} 开始')
        time.sleep(self.delay)
        print(f'线程 {self.name} 结束')

# 使用
threads = [MyThread(f'Thread-{i}', i) for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()

# 线程属性
t = threading.current_thread()
print(f'当前线程: {t.name}')
print(f'线程是否存活: {t.is_alive()}')
print(f'活动线程数: {threading.active_count()}')
```

### 线程同步

```python
import threading

# Lock - 互斥锁
lock = threading.Lock()
counter = 0

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f'计数器: {counter}')  # 500000

# RLock - 可重入锁
rlock = threading.RLock()

def nested_lock():
    with rlock:
        print('外层锁')
        with rlock:
            print('内层锁')

# Semaphore - 信号量
semaphore = threading.Semaphore(3)  # 允许3个线程同时访问

def limited_access(name):
    with semaphore:
        print(f'{name} 获得访问权')
        time.sleep(1)
        print(f'{name} 释放访问权')

threads = [threading.Thread(target=limited_access, args=(f'T{i}',)) for i in range(5)]
for t in threads:
    t.start()

# Event - 事件
event = threading.Event()

def waiter():
    print('等待事件...')
    event.wait()
    print('事件已设置')

def setter():
    time.sleep(2)
    event.set()
    print('事件已触发')

threading.Thread(target=waiter).start()
threading.Thread(target=setter).start()

# Condition - 条件变量
condition = threading.Condition()
items = []

def producer():
    with condition:
        items.append('item')
        print('生产者: 添加项目')
        condition.notify()

def consumer():
    with condition:
        while not items:
            condition.wait()
        item = items.pop()
        print(f'消费者: 获取 {item}')
```

### 线程池

```python
from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    print(f'处理任务 {n}')
    time.sleep(1)
    return n * n

# 使用线程池
with ThreadPoolExecutor(max_workers=3) as executor:
    # 提交任务
    futures = [executor.submit(task, i) for i in range(5)]
    
    # 获取结果
    for future in futures:
        result = future.result()
        print(f'结果: {result}')

# map 方法
with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(task, range(5)))
    print(f'所有结果: {results}')
```

## 0x02. 多进程

### 基本使用

```python
from multiprocessing import Process
import os
import time

def worker(name):
    print(f'进程 {name} (PID: {os.getpid()}) 开始')
    time.sleep(1)
    print(f'进程 {name} 结束')

# 创建进程
if __name__ == '__main__':
    processes = [Process(target=worker, args=(f'P{i}',)) for i in range(3)]
    
    for p in processes:
        p.start()
    
    for p in processes:
        p.join()
    
    print('所有进程完成')
```

### 进程间通信

```python
from multiprocessing import Process, Queue, Pipe, Value, Array
import time

# Queue - 队列通信
def producer(queue):
    for i in range(5):
        queue.put(i)
        print(f'生产: {i}')
    queue.put(None)  # 结束信号

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f'消费: {item}')

if __name__ == '__main__':
    queue = Queue()
    p1 = Process(target=producer, args=(queue,))
    p2 = Process(target=consumer, args=(queue,))
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()

# Pipe - 管道通信
def sender(conn):
    conn.send('Hello from sender')
    conn.close()

def receiver(conn):
    msg = conn.recv()
    print(f'收到: {msg}')

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p1 = Process(target=sender, args=(child_conn,))
    p2 = Process(target=receiver, args=(parent_conn,))
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()

# Value 和 Array - 共享内存
def worker(num):
    num.value = 3.14

if __name__ == '__main__':
    num = Value('d', 0.0)  # 'd' 表示 double
    p = Process(target=worker, args=(num,))
    p.start()
    p.join()
    print(f'值: {num.value}')  # 3.14
```

### 进程池

```python
from multiprocessing import Pool
import time

def task(n):
    print(f'处理任务 {n}')
    time.sleep(1)
    return n * n

if __name__ == '__main__':
    with Pool(processes=4) as pool:
        # map 方法
        results = pool.map(task, range(10))
        print(f'结果: {results}')
        
        # apply_async 方法
        results = [pool.apply_async(task, (i,)) for i in range(10)]
        output = [r.get() for r in results]
        print(f'异步结果: {output}')

# 进程池执行器
from concurrent.futures import ProcessPoolExecutor

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(task, range(10)))
        print(f'结果: {results}')
```

## 0x03. 异步编程

### async/await

```python
import asyncio

async def hello():
    print('Hello')
    await asyncio.sleep(1)
    print('World')

# 运行协程
asyncio.run(hello())

# 多个协程并发执行
async def main():
    await asyncio.gather(
        hello(),
        hello(),
        hello()
    )

asyncio.run(main())
```

### 异步任务

```python
import asyncio

async def fetch_data(url, delay):
    print(f'开始获取 {url}')
    await asyncio.sleep(delay)
    print(f'完成获取 {url}')
    return f'Data from {url}'

async def main():
    # 创建任务
    task1 = asyncio.create_task(fetch_data('url1', 2))
    task2 = asyncio.create_task(fetch_data('url2', 1))
    
    # 等待任务完成
    result1 = await task1
    result2 = await task2
    
    print(result1)
    print(result2)

asyncio.run(main())

# gather - 并发执行多个协程
async def main():
    results = await asyncio.gather(
        fetch_data('url1', 2),
        fetch_data('url2', 1),
        fetch_data('url3', 3)
    )
    print(results)

asyncio.run(main())

# as_completed - 按完成顺序获取结果
async def main():
    tasks = [
        fetch_data('url1', 2),
        fetch_data('url2', 1),
        fetch_data('url3', 3)
    ]
    
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print(f'完成: {result}')

asyncio.run(main())
```

### 异步上下文管理器

```python
import asyncio

class AsyncResource:
    async def __aenter__(self):
        print('获取资源')
        await asyncio.sleep(0.1)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print('释放资源')
        await asyncio.sleep(0.1)
    
    async def use(self):
        print('使用资源')
        await asyncio.sleep(0.1)

async def main():
    async with AsyncResource() as resource:
        await resource.use()

asyncio.run(main())

# 异步生成器
async def async_range(n):
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i

async def main():
    async for i in async_range(5):
        print(i)

asyncio.run(main())
```

### 异步队列

```python
import asyncio

async def producer(queue):
    for i in range(5):
        await queue.put(i)
        print(f'生产: {i}')
        await asyncio.sleep(0.1)

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f'消费: {item}')
        queue.task_done()

async def main():
    queue = asyncio.Queue(maxsize=3)
    
    # 启动生产者和消费者
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))
    
    # 等待生产者完成
    await producer_task
    
    # 等待队列处理完毕
    await queue.join()
    
    # 取消消费者
    consumer_task.cancel()

asyncio.run(main())
```

## 0x04. 选择并发模型

```python
"""
选择并发模型的建议：

1. 多线程 (threading)
   - 适用于 I/O 密集型任务
   - 网络请求、文件操作
   - 共享内存，但需要同步

2. 多进程 (multiprocessing)
   - 适用于 CPU 密集型任务
   - 数学计算、图像处理
   - 避免 GIL 限制

3. 异步 (asyncio)
   - 适用于大量 I/O 操作
   - 网络服务器、爬虫
   - 单线程，高并发

4. 线程池/进程池 (concurrent.futures)
   - 简化并发编程
   - 自动管理资源
"""

# I/O 密集型任务 - 使用多线程
from concurrent.futures import ThreadPoolExecutor
import requests

def fetch_url(url):
    response = requests.get(url)
    return len(response.content)

urls = ['http://example.com'] * 10
with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(fetch_url, urls))

# CPU 密集型任务 - 使用多进程
from concurrent.futures import ProcessPoolExecutor

def heavy_computation(n):
    return sum(i * i for i in range(n))

numbers = [1000000] * 10
with ProcessPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(heavy_computation, numbers))

# 高并发 I/O - 使用异步
import asyncio
import aiohttp

async def fetch_url_async(session, url):
    async with session.get(url) as response:
        return len(await response.read())

async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['http://example.com'] * 10
        tasks = [fetch_url_async(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

asyncio.run(main())
```

## 参考
1. [Python 官方文档 - threading](https://docs.python.org/3/library/threading.html)
2. [Python 官方文档 - multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
3. [Python 官方文档 - asyncio](https://docs.python.org/3/library/asyncio.html)
4. [Python 官方文档 - concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)