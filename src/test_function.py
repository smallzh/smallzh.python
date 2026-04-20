"""
# test_function.py
涵盖核心 Python 函数特性测试，使用 pytest 风格，确保自包含且无外部依赖。
"""

import asyncio
from typing import List, Dict, Tuple, Optional, Union
from functools import wraps, lru_cache


class TestBasicFunction:
    def test_def_and_call(self):
        def add(a, b):
            return a + b
        assert add(2, 3) == 5

    def test_return_multiple_values(self):
        def divmod_pair(a, b):
            return divmod(a, b)
        q, r = divmod_pair(7, 3)
        assert (q, r) == (2, 1)


class TestPositionalArgs:
    def test_positional_matching(self):
        def f(a, b, c):
            return a + b + c
        assert f(1, 2, 3) == 6


class TestDefaultArgs:
    def test_default_values(self):
        def concat(a, b='b'):
            return a + b
        assert concat('a') == 'ab'
        assert concat('a', 'c') == 'ac'

    def test_mutable_default_trap(self):
        def append_with_list(val, lst=None):
            if lst is None:
                lst = []
            lst.append(val)
            return lst
        assert append_with_list(1) == [1]
        assert append_with_list(2) == [2]

    def test_mutable_default_shared(self):
        def append_shared(val, lst=[]):  # 不推荐的写法，展示坑
            lst.append(val)
            return lst
        a = append_shared(1)
        b = append_shared(2)
        assert a == [1, 2] and b == [1, 2]


class TestKeywordArgs:
    def test_keyword_order(self):
        def f(a, b=2, c=3):
            return a + b + c
        assert f(1, c=5, b=2) == 8

    def test_mix_args_and_kwargs(self):
        def g(a, b=1, *, c=2):
            return a + b + c
        assert g(1, 2, c=3) == 6


class TestVarArgs:
    def test_args_and_kwargs(self):
        def h(*args, **kwargs):
            return args, kwargs
        r_args, r_kwargs = h(1, 2, x=3)
        assert r_args == (1, 2)
        assert r_kwargs == {'x': 3}


class TestKeywordOnly:
    def test_keyword_only(self):
        def f(a, *, b=2):
            return a + b
        assert f(3, b=4) == 7


class TestPositionalOnly:
    def test_positional_only_and_error(self):
        def g(a, b, /, c):
            return a + b + c
        assert g(1, 2, 3) == 6
        try:
            g(a=1, b=2, c=3)  # 应抛出 TypeError
        except TypeError:
            pass
        else:
            assert False


class TestUnpackArgs:
    def test_unpacking(self):
        def f(a, b, c, d):
            return a + b + c + d
        assert f(1, 2, 3, 4) == 10
        assert f(*[1, 2], *[3, 4]) == 10
        d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        assert f(**d) == 10
        assert f(1, *[2, 3], d=4) == 10


class TestLambda:
    def test_basic_lambda_and_defaults(self):
        f = lambda x: x + 1
        assert f(5) == 6
        g = lambda x, y=10: x + y
        assert g(5) == 15
        vals = list(map(lambda n: n * n, [1, 2, 3]))
        assert vals == [1, 4, 9]


class TestClosure:
    def test_basic_closure(self):
        def make_multiplier(n):
            def inner(x):
                return n * x
            return inner
        times3 = make_multiplier(3)
        assert times3(4) == 12

    def test_nonlocal_counter(self):
        def make_counter():
            count = 0
            def inc():
                nonlocal count
                count += 1
                return count
            return inc
        c = make_counter()
        assert c() == 1
        assert c() == 2


class TestDecorator:
    def test_basic_decorator_and_wraps(self):
        def deco(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                wrapper.calls += 1
                return fn(*args, **kwargs)
            wrapper.calls = 0
            return wrapper

        @deco
        def add(a, b):
            return a + b
        assert add(1, 2) == 3
        assert add.calls == 1

    def test_decorator_with_args(self):
        def decorator_with_arg(n):
            def deco(fn):
                @wraps(fn)
                def wrapper(*args, **kwargs):
                    return fn(*args, **kwargs) + n
                return wrapper
            return deco

        @decorator_with_arg(5)
        def base(x):
            return x
        assert base(3) == 8


class TestGeneratorFunction:
    def test_yield_and_generator_expression(self):
        def gen():
            yield 1
            yield 2
        assert list(gen()) == [1, 2]
        gen_exp = (x * x for x in range(3))
        assert list(gen_exp) == [0, 1, 4]

    def test_fibonacci_generator(self):
        def fib(n):
            a, b = 0, 1
            for _ in range(n):
                yield a
                a, b = b, a + b
        assert list(fib(5)) == [0, 1, 1, 2, 3]


class TestRecursion:
    def test_factorial(self):
        def fact(n):
            if n <= 1:
                return 1
            return n * fact(n - 1)
        assert fact(5) == 120

    def test_fibonacci_recursion_and_cache(self):
        @lru_cache(maxsize=None)
        def fib(n):
            if n < 2:
                return n
            return fib(n - 1) + fib(n - 2)
        assert fib(10) == 55


class TestTypeAnnotation:
    def test_basic_annotations(self):
        def add(a: int, b: int) -> int:
            return a + b
        ann = add.__annotations__
        assert ann['a'] is int and ann['b'] is int and ann['return'] is int

    def test_typing_hints(self):
        def f1(li: List[int]) -> List[int]:
            return [i * 2 for i in li]
        assert f1([1, 2])[1] == 4

        def f2(d: Dict[str, int]) -> int:
            return d.get('x', 0)
        assert f2({'x': 5}) == 5

        def f3(t: Tuple[int, str]) -> Tuple[int, str]:
            return t
        assert f3((1, 'a')) == (1, 'a')

        def f4(opt: Optional[int]) -> Union[int, None]:
            return opt
        assert f4(None) is None

    def test_union_and_pipe_annotation(self):
        def f(x: int | str) -> bool:
            return isinstance(x, int)
        assert f(3) is True
        assert f('a') is False


class TestDocstring:
    def test_function_docstring(self):
        def greet():
            """简单问候函数"""
            return 'hi'
        assert greet.__doc__ is not None and '简单' in greet.__doc__


class TestAsyncFunction:
    def test_async_basic_and_gather(self):
        async def add(a, b):
            return a + b

        async def main():
            r1 = await add(2, 3)
            r2, r3 = await asyncio.gather(add(4, 1), add(5, 5))
            return r1, r2, r3

        res = asyncio.run(main())
        assert res == (5, 5, 10)
