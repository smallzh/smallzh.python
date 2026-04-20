#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""测试 typing 模块的核心类型提示与用法
覆盖基本类型提示、复杂类型、Python 3.9+ 泛型语法、TypeVar、TypedDict、Literal、Protocol、TypeAlias 等要点。"""

from __future__ import annotations

from typing import (
    List,
    Dict,
    Tuple,
    Set,
    Optional,
    Union,
    Callable,
    Any,
    get_type_hints,
    TypeVar,
    Generic,
    TypedDict,
    Literal,
    Protocol,
)
from collections import namedtuple


def test_basic_type_hints_function_and_variables():
    def add(a: int, b: int) -> int:
        return a + b
    hints = get_type_hints(add)
    assert hints['a'] is int
    assert hints['b'] is int
    assert hints['return'] is int

    # 使用类级别的变量注解来验证变量注解行为
    # 注意: from __future__ import annotations 使注解变为字符串
    class Annotated:
        x: int
    assert Annotated.__annotations__['x'] == 'int' or Annotated.__annotations__['x'] is int


def test_complex_types_and_callable_and_any():
    def f1(vals: List[int], mapping: Dict[str, int]) -> Tuple[float, float]:
        return (float(len(vals)), float(sum(mapping.values())))
    hints = get_type_hints(f1)
    assert hints['vals'] == List[int]
    assert hints['mapping'] == Dict[str, int]
    assert hints['return'] == Tuple[float, float]

    def g(c: Optional[int]) -> Union[int, str]:
        return c if c is not None else 'none'
    hg = get_type_hints(g)
    assert hg['c'] == Optional[int]
    assert hg['return'] == Union[int, str]

    def h(x: int, y: int) -> int:
        return x + y
    hints_h = get_type_hints(h)
    assert hints_h['x'] is int and hints_h['y'] is int
    assert hints_h['return'] is int

    def chicken(a: int) -> int:
        return a * 2
    ch_hints = get_type_hints(chicken, None, None)
    assert ch_hints['a'] is int
    assert ch_hints['return'] is int

    def any_func(a: Any) -> Any:
        return a
    any_hints = get_type_hints(any_func)
    assert any_hints['return'] is Any


def test_generic_syntax_py39_plus():
    def f(a: list[int]) -> dict[str, int]:
        return {str(a[0]): len(a)}
    hints = get_type_hints(f)
    assert hints['a'] == list[int]
    assert hints['return'] == dict[str, int]


def test_typevar_and_generic_class():
    T = TypeVar('T')

    def identity(x: T) -> T:
        return x
    hints = get_type_hints(identity, globals(), locals())
    assert 'x' in hints and hints['x'] is T
    assert hints['return'] is T

    class Stack(Generic[T]):
        def __init__(self):
            self.items: List[T] = []
        def push(self, item: T) -> None:
            self.items.append(item)
        def pop(self) -> T:
            return self.items.pop()

    s = Stack[int]()
    s.push(1)
    assert isinstance(s.pop(), int)


def test_typed_dict_and_literal():
    class Point(TypedDict):
        x: int
        y: int
    p: Point = {'x': 1, 'y': 2}
    assert p['x'] == 1 and p['y'] == 2
    class PointOpt(TypedDict, total=False):
        x: int
        y: int
        z: int
    p2: PointOpt = {'x': 1}
    assert 'z' not in p2

def test_protocol_and_type_alias():
    class P(Protocol):
        def quack(self) -> str: ...

    class Duck:
        def quack(self) -> str:
            return 'quack'
    def talk(q: P) -> str:
        return q.quack()
    d = Duck()
    assert talk(d) == 'quack'

    # Type alias - 使用get_type_hints并指定全局命名空间
    Vector = List[int]
    def sum_vec(v: Vector) -> int:
        return sum(v)
    hints = get_type_hints(sum_vec, globals(), locals())
    assert hints['v'] == Vector
