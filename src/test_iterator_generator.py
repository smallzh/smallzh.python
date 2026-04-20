#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试迭代器与生成器相关知识点，覆盖迭代协议、内置迭代器、生成器及 itertools。
文档对齐：依据 docs/iterator_generator.md 的知识点编写测试用例。
"""
import itertools
from collections.abc import Iterator, Iterable


class TestIteratorProtocol:
    def test_custom_iterator_and_reverse(self):
        class MyIter:
            def __init__(self, n):
                self.n = n
                self.i = 0
            def __iter__(self):
                return self
            def __next__(self):
                if self.i >= self.n:
                    raise StopIteration
                val = self.i
                self.i += 1
                return val
        it = MyIter(3)
        assert next(it) == 0
        assert next(it) == 1
        assert next(it) == 2

        # 重新创建后再测试完成
        it2 = MyIter(2)
        assert list(it2) == [0, 1]

    def test_reverse_iterator_class_and_iterable_vs_iterator(self):
        class ReverseListIterator:
            def __init__(self, data):
                self.data = data
            def __iter__(self):
                for i in range(len(self.data) - 1, -1, -1):
                    yield self.data[i]
        assert list(ReverseListIterator([1, 2, 3])) == [3, 2, 1]

        assert isinstance([1, 2, 3], Iterable)
        assert not isinstance([1, 2, 3], Iterator)
        it = iter([1, 2, 3])
        assert isinstance(it, Iterator)

    def test_builtin_iterator_functions(self):
        it = iter([1, 2, 3])
        assert next(it) == 1
        assert list(map(str, [4, 5])) == ["4", "5"]
        assert list(enumerate(["a", "b"])) == [(0, "a"), (1, "b")]
        assert list(zip([1, 2], ["a", "b", "c"])) == [(1, "a"), (2, "b")]
        assert list(filter(None, [0, 1, 2, ""])) == [1, 2]

    def test_generator_function(self):
        def count_up_to(n):
            for i in range(n):
                yield i
        g = count_up_to(3)
        assert isinstance(g, Iterator)
        assert list(g) == [0, 1, 2]

        def fibonacci(limit):
            a, b = 0, 1
            for _ in range(limit):
                yield b
                a, b = b, a + b
        assert list(fibonacci(5)) == [1, 1, 2, 3, 5]

        # 惰性求值示例：生成器表达式与求和对比
        assert sum(x * x for x in range(5)) == 30
        # 生成器的 send/throw/close 行为演示
        def accumulator():
            total = 0
            while True:
                x = yield total
                if x is None:
                    continue
                total += x
        ag = accumulator()
        assert next(ag) == 0
        assert ag.send(5) == 5
        assert ag.send(3) == 8
        ag.close()

        def gen_with_error():
            try:
                yield "start"
                yield "middle"
            except ValueError:
                yield "caught"
        g2 = gen_with_error()
        assert next(g2) == "start"
        assert g2.throw(ValueError("err")) == "caught"

        # 关闭生成器应正常完成
        g3 = (i for i in range(2))
        g3.close()

    def test_generator_expression_and_comprehensions(self):
        g = (x * x for x in range(5))
        assert list(g) == [0, 1, 4, 9, 16]
        # 在函数中使用生成器表达式
        assert sum(x * x for x in range(5)) == 30
        # 链式生成器与列表推导对比
        assert list((y for x in range(3) for y in range(x))) == [0, 0, 1]
        assert list([x * x for x in range(5)]) == [0, 1, 4, 9, 16]

    def test_comprehensions_and_tools(self):
        # 推导式
        assert [i * 2 for i in range(4)] == [0, 2, 4, 6]
        assert {i: i * i for i in range(4)} == {0: 0, 1: 1, 2: 4, 3: 9}
        assert {i for i in range(5) if i % 2 == 0} == {0, 2, 4}
        assert [(i, j) for i in range(2) for j in range(2)] == [(0, 0), (0, 1), (1, 0), (1, 1)]
        assert [i for i in range(5) if i % 2 == 0] == [0, 2, 4]

        # itertools 常用函数
        assert list(itertools.islice(itertools.count(0), 3)) == [0, 1, 2]
        # cycle 与 islice 的组合
        c = itertools.cycle([1, 2])
        assert list(itertools.islice(c, 4)) == [1, 2, 1, 2]
        assert list(itertools.repeat("A", 3)) == ["A", "A", "A"]
        assert list(itertools.chain([1, 2], [3, 4])) == [1, 2, 3, 4]
        assert list(itertools.islice(range(10), 3)) == [0, 1, 2]
        assert list(itertools.filterfalse(bool, [0, 1, 2, "", None, "x"])) == [0, "", None]
        # takewhile 与 dropwhile
        assert list(itertools.takewhile(lambda x: x < 3, [0, 1, 2, 3, 0])) == [0, 1, 2]
        assert list(itertools.dropwhile(lambda x: x < 3, [1, 2, 3, 0])) == [3, 0]
        # starmap
        assert list(itertools.starmap(pow, [(2, 3), (3, 2)])) == [8, 9]
        # product、permutations、combinations
        assert list(itertools.product([1, 2], ['a', 'b'])) == [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
        assert list(itertools.permutations([1, 2, 3], 2)) == [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
        assert list(itertools.combinations([1, 2, 3], 2)) == [(1, 2), (1, 3), (2, 3)]
        # groupby：对连续的键进行分组
        data = [1, 1, 2, 2, 3]
        groups = [(k, list(g)) for k, g in itertools.groupby(data)]
        assert groups == [(1, [1, 1]), (2, [2, 2]), (3, [3])]
