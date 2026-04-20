#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试核心 Python 知识点：类型转换、数学、序列、对象、字符、迭代器等。

说明: pytest 风格测试，所有断言均使用内置类型与函数，无外部依赖。
文档对齐：依据 docs/inner_function.md 的知识点编排测试用例。
"""

import itertools
from collections.abc import Iterable, Iterator


class TestTypeConversion:
    def test_int_conversions(self):
        # 字符串十进制转换
        assert int("42") == 42
        # 指定进制：二进制/八进制/十六进制(使用 base=0 自动识别前缀)
        assert int("101", 2) == 5
        assert int("12", 8) == 10
        assert int("FF", 16) == 255
        # 浮点数转整数会截断小数部分
        assert int(3.9) == 3
        # 布尔值转整数
        assert int(True) == 1
        assert int(False) == 0

    def test_float_and_bool_conversions(self):
        assert float("3.14") == 3.14
        assert float("2e1") == 20.0
        assert float(True) == 1.0
        assert float(False) == 0.0

    def test_str_and_other_conversions(self):
        assert str(123) == "123"
        assert str(3.14) == "3.14"
        assert str([1, 2]) == "[1, 2]"
        assert bool(0) is False
        assert bool(0.0) is False
        assert bool("") is False
        assert bool([]) is False
        assert bool({}) is False
        assert bool(None) is False
        assert bool("非空") is True

    def test_sequence_and_mapping_conversions(self):
        assert list("abc") == ["a", "b", "c"]
        assert list(range(3)) == [0, 1, 2]
        assert tuple([1, 2, 3]) == (1, 2, 3)
        assert set([1, 1, 2]) == {1, 2}
        assert dict([(1, 2), (3, 4)]) == {1: 2, 3: 4}
        assert dict(a=1, b=2) == {"a": 1, "b": 2}
        assert dict.fromkeys(["a", "b"], 0) == {"a": 0, "b": 0}


class TestMathFunctions:
    def test_abs_and_round_and_pow(self):
        assert abs(-3) == 3
        assert abs(3.5) == 3.5
        assert abs(3 + 4j) == 5.0

        # 四舍五入以及银行家舍入法
        assert round(1.5) == 2
        assert round(2.5) == 2
        assert round(1.0) == 1
        # 指定小数位
        assert round(1.25, 1) in (1.2, 1.3)
        # 幂运算，包括三参数模式
        assert pow(2, 3) == 8
        assert pow(2, 3, 5) == 3

    def test_divmod_sum_min_max(self):
        assert divmod(9, 4) == (2, 1)
        assert sum([1, 2, 3]) == 6
        assert sum([1, 2, 3], 10) == 16
        assert min([3, 1, 4]) == 1
        assert max([3, 1, 4]) == 4
        assert max(["a", "bb", "ccc"], key=len) == "ccc"


class TestSequenceFunctions:
    def test_len_and_range_and_sorted(self):
        assert len("abc") == 3
        assert len([1, 2, 3]) == 3
        assert list(range(0, 3)) == [0, 1, 2]
        assert list(range(2, 5)) == [2, 3, 4]
        assert list(range(0, 5, 2)) == [0, 2, 4]
        assert sorted([3, 1, 2]) == [1, 2, 3]
        assert sorted(["b", "aa", "ccc"], key=len) == ["b", "aa", "ccc"]
        assert sorted([3, 1, 2], reverse=True) == [3, 2, 1]

    def test_reversed_enumerate_zip_and_map_filter(self):
        assert list(reversed([1, 2, 3])) == [3, 2, 1]
        assert list(enumerate(["a", "b"], start=1)) == [(1, "a"), (2, "b")]
        assert list(zip([1, 2], ["a", "b", "c"])) == [(1, "a"), (2, "b")]
        assert list(map(str, [1, 2])) == ["1", "2"]
        assert list(map(lambda x, y: x + y, [1, 2], [3, 4])) == [4, 6]
        assert list(filter(None, [0, 1, 2, "", None, "x"])) == [1, 2, "x"]


class TestObjectFunctions:
    def test_type_isinstance_id_hash_and_attrs(self):
        assert type(5) is int
        Dynamic = type("DynamicClass", (), {})
        obj = Dynamic()
        assert isinstance(obj, Dynamic)
        assert isinstance(5, (int, float))
        assert id(obj) is not None
        assert isinstance(hash("abc"), int)

        class Sample:
            pass
        assert not hasattr(Sample, "x")
        setattr(Sample, "x", 10)
        assert hasattr(Sample, "x")
        assert getattr(Sample, "x") == 10
        delattr(Sample, "x")
        assert not hasattr(Sample, "x")
        assert callable(len)
        assert not callable(5)


class TestCharacterFunctions:
    def test_chr_ord_repr_ascii(self):
        assert chr(97) == "a"
        assert ord("a") == 97
        assert repr("hello") == "'hello'"
        assert ascii("é") == "'\\xe9'"


class TestIteratorFunctions:
    def test_iter_and_next_and_all_any(self):
        it = iter([1, 2, 3])
        assert next(it) == 1
        assert next(it) == 2
        assert next(it) == 3
        try:
            next(it)
            assert False, "应抛出 StopIteration"
        except StopIteration:
            pass
        assert all([True, 1, 3]) is True
        assert all([]) is True
        assert any([0, 0, 1]) is True
        assert any([]) is False


class TestOtherFunctions:
    def test_vars_dir_globals_locals(self):
        class LocalClass:
            pass
        local = LocalClass()
        d = vars()
        assert isinstance(d, dict)
        # dir 对象属性列表的基本存在性
        assert '__class__' in dir(local)
        g = globals()
        l = locals()
        assert isinstance(g, dict)
        assert isinstance(l, dict)
