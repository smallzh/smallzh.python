# -*- coding: utf-8 -*-
"""
test_data_type.py
基于 docs/data_type.md 的核心 Python 知识点单元测试。
使用 pytest 风格，确保在 Python 3.13+ 下通过。
所有断言均为内建类型和运算的正确性测试。
"""
import math
import datetime as _dt
import cmath
import pytest


class TestIntInteger:
    def test_decimal_binary_octal_hex_and_arithmetic(self):
        """整数：十进制/二进制/八进制/十六进制表示及下划线分隔大数字，算术运算"""
        a = 255
        assert a == 0b11111111
        assert a == 0o377
        assert a == 0xFF
        n = 1_234_567
        assert n == 1234567
        # 算术运算
        assert (7 + 3) == 10
        assert (10 - 2) == 8
        assert (3 * 5) == 15
        assert (7 / 2) == 3.5
        assert (7 // 2) == 3


class TestFloat:
    def test_basic_float_and_scientific_and_precision(self):
        """浮点数：基本数值、科学计数法、精度问题与 isclose"""
        f = 0.1 + 0.2
        assert f != 0.3
        assert math.isclose(f, 0.3)
        assert 1.5e3 == 1500.0
        # isclose 的自定义容忍度测试
        assert math.isclose(0.15, 0.15, rel_tol=1e-9)


class TestComplex:
    def test_creation_properties_operations_and_abs(self):
        """复数：创建、属性、运算和模"""
        z1 = 3 + 4j
        z2 = complex(3, 4)
        assert z1 == z2
        assert z1.real == 3
        assert z1.imag == 4
        assert z1 + z2 == 6 + 8j
        assert z1 * z2 == -7 + 24j
        assert abs(z1) == 5.0


class TestBool:
    def test_boolean_values_and_truthiness(self):
        """布尔类型：真值与布尔运算、真值测试"""
        assert bool(True) is True
        assert bool(False) is False
        assert (True and False) is False
        assert (True or False) is True
        assert (not True) is False
        # 真值测试
        assert bool(0) is False
        assert bool(0.0) is False
        assert bool('') is False
        assert bool([]) is False
        assert bool({}) is False
        assert bool(None) is False
        # 非假值
        assert bool(1) is True
        assert bool('hello') is True
        assert bool([1, 2]) is True


class TestList:
    def test_creation_access_modification_and_slicing_and_comp(self):
        """列表：创建/访问/修改、切片、推导"""
        l = [1, 2, 3]
        l.append(4)
        l.insert(1, 'a')
        l.extend([5, 6])
        l.remove('a')
        last = l.pop()
        assert last == 6
        del l[0]
        assert l == [2, 3, 4, 5]
        # 切片
        base = [10, 20, 30, 40, 50]
        assert base[1:4] == [20, 30, 40]
        assert base[::2] == [10, 30, 50]
        assert base[::-1] == [50, 40, 30, 20, 10]
        # 列表推导
        squares = [x * x for x in range(5)]
        assert squares == [0, 1, 4, 9, 16]
        # 基本聚合
        nums = [3, 1, 2, 3, 4]
        assert len(nums) == 5
        assert min(nums) == 1
        assert max(nums) == 4
        assert sum(nums) == 13
        sorted_nums = sorted(nums)
        assert sorted_nums == [1, 2, 3, 3, 4]
        assert nums.count(3) == 2
        assert nums.index(3) == 0


class TestTuple:
    def test_creation_access_unpack_and_immutability_and_dict_key(self):
        """元组：创建、访问、不可变、可作为字典键"""
        t = (1, 2, 3)
        t1 = (1,)
        assert t[0] == 1
        a, b, c = t
        assert (a, b, c) == t
        with pytest.raises(TypeError):
            t[0] = 9
        d = {t: 'value'}
        assert d[(1, 2, 3)] == 'value'


class TestDict:
    def test_operations_and_comprehensions_and_merge(self):
        """字典：创建、访问、增删改、遍历、推导、合并"""
        d = {'a': 1, 'b': 2}
        assert d.get('a') == 1
        assert d.get('c', 3) == 3
        d['c'] = 3
        del d['b']
        assert 'b' not in d
        popped = d.pop('a')
        assert popped == 1
        assert set(d.keys()) == {'c'}
        assert set(d.values()) == {3}
        assert list(d.items()) == [('c', 3)]
        comp = {k: v for k, v in [('x', 9), ('y', 8)]}
        merged = {**{'a': 0}, **comp}
        assert merged == {'a': 0, 'x': 9, 'y': 8}


class TestSet:
    def test_basic_and_operations_and_comprehension_and_dedup(self):
        """集合：创建、基本操作、集合运算、推导、去重"""
        s = set([1, 2, 2, 3])
        assert s == {1, 2, 3}
        s.add(4)
        s.remove(4)
        s.discard(99)  # 不抛异常
        s1, s2 = {1, 2, 3}, {2, 3, 4}
        assert (s1 | s2) == {1, 2, 3, 4}
        assert (s1 & s2) == {2, 3}
        assert (s1 - s2) == {1}
        assert (s1 ^ s2) == {1, 4}
        s_comp = {x for x in [1, 2, 2, 3]}
        assert s_comp == {1, 2, 3}
        assert len(set([1, 1, 2])) == 2


class TestFrozenset:
    def test_immutable_and_dictionary_key(self):
        """不可变集合：不可变性与字典键属性"""
        fs = frozenset([1, 2, 3])
        with pytest.raises(AttributeError):
            fs.add(4)
        d = {fs: 'yes'}
        assert d[frozenset([3, 2, 1])] == 'yes'


class TestNone:
    def test_none_identity_and_default_usage(self):
        """None：None 是 None、is 判断、默认参数示例"""
        assert None is None
        assert (None == None) is True
        def f(x=None):
            return x
        assert f() is None


class TestTypeCheck:
    def test_type_and_conversion(self):
        """类型检查与基本类型转换"""
        assert type(1) is int
        assert isinstance(3.14, float)
        assert isinstance("s", str)
        assert int("42") == 42
        assert float("3.14") == 3.14
        assert str(123) == "123"
        assert list((1, 2, 3)) == [1, 2, 3]
        assert tuple([1, 2, 3]) == (1, 2, 3)
        assert set([1, 1, 2]) == {1, 2}
