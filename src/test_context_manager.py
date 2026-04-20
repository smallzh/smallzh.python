#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""测试核心 Python 上下文管理相关特性

基于文档：context_manager.md，覆盖 with 语句、类实现的上下文管理器、contextlib.contextmanager、suppress、ExitStack 及常用上下文管理器等要点。
测试均以 pytest 风格编写，依赖仅为 Python 标准库。
"""

import contextlib
import os
import time
import threading
import tempfile
from contextlib import ExitStack


def test_with_statement_basic():
    """测试 with 语句的基本用法：自动关闭资源，如文件对象
    1) with open 自动关闭
    2) 可以同时使用多个上下文管理器
    """
    # 基本的文件上下文：写入再读取，确保不需要显式关闭
    with tempfile.NamedTemporaryFile("w", delete=False) as tf:
        tf.write("hello")
        name = tf.name
    with open(name, "r") as f:
        data = f.read()
    assert data == "hello"
    os.remove(name)

    # 多个上下文管理器同时使用
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "a.txt")
        with open(path, "w") as f:
            f.write("ok")
        assert os.path.exists(path)


def test_class_context_manager_enter_exit():
    """测试自定义上下文管理类实现 __enter__/__exit__ 的行为
    - __exit__ 的三个参数表示异常信息：exc_type, exc_val, exc_tb
    - 返回 True 可抑制异常，返回 False/None 则传播异常
    """

    class CMSuppress:
        def __init__(self):
            self.entered = False
            self.exited_with = None

        def __enter__(self):
            self.entered = True
            return self

        def __exit__(self, exc_type, exc, tb):
            # 记录异常信息，并抑制异常
            self.exited_with = (exc_type, exc, tb)
            return True

    cm = CMSuppress()
    with cm:
        raise ValueError("boom")
    # 断言 enter/exit 行为，以及 exit 收集到的异常信息（被抑制）
    assert cm.entered is True
    assert cm.exited_with[0] is ValueError


def test_class_context_manager_propagates_false():
    """__exit__ 返回 False 时会把异常抛出"""

    class CMNoSuppress:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

    started = False
    try:
        with CMNoSuppress():
            started = True
            raise RuntimeError("fail")
    except RuntimeError:
        # 期望传播异常
        assert True
    else:
        assert False


def test_contextlib_contextmanager_and_yield():
    """contextmanager 装饰器 + yield 的用法，确保清理逻辑执行"""

    counter = {"entered": 0, "exited": 0}

    @contextlib.contextmanager
    def timer_marker():
        counter["entered"] += 1
        try:
            yield
        finally:
            counter["exited"] += 1

    with timer_marker():
        pass
    assert counter["entered"] == 1 and counter["exited"] == 1


def test_contextlib_suppress():
    """contextlib.suppress 用于抑制特定异常类型"""
    import contextlib

    # 抑制匹配的异常
    with contextlib.suppress(KeyError):
        raise KeyError("ignore me")

    # 不匹配的异常应当抛出
    try:
        with contextlib.suppress(KeyError):
            raise ValueError("not suppressed")
        assert False
    except ValueError:
        assert True


def test_exit_stack_dynamic_contexts():
    """ExitStack 动态管理多个上下文对象"""
    logs = []

    class CM:
        def __init__(self, v):
            self.v = v
        def __enter__(self):
            logs.append(("enter", self.v))
            return self
        def __exit__(self, exc_type, exc, tb):
            logs.append(("exit", self.v))
            return False

    with ExitStack() as stack:
        stack.enter_context(CM(1))
        stack.enter_context(CM(2))
    assert logs == [("enter", 1), ("enter", 2), ("exit", 2), ("exit", 1)]


def test_common_context_managers_basic():
    """常用上下文管理器：threading.Lock / NamedTemporaryFile / TemporaryDirectory"""
    import threading
    import tempfile
    import os

    # threading.Lock
    lock = threading.Lock()
    assert not lock.locked()
    with lock:
        assert lock.locked()
    assert not lock.locked()

    # NamedTemporaryFile
    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        f.write("data")
        name = f.name
    with open(name, "r") as f2:
        assert f2.read() == "data"
    os.remove(name)

    # TemporaryDirectory
    with tempfile.TemporaryDirectory() as td:
        assert os.path.isdir(td)

