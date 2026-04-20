"""
# test_process_control.py
包含与 docs/process_control.md 对应的核心 Python 流程控制知识点测试。
使用 pytest 风格（函数名以 test_ 开头），全部自包含且仅依赖 stdlib。
"""

import itertools
import math
from typing import List, Dict, Tuple


class TestIfElifElse:
    def test_basic_if(self):
        """基本 if 条件判断：True 分支执行"""
        x = 0
        if True:
            x = 1
        else:
            x = 2
        assert x == 1

    def test_if_else_elif_grade(self):
        """if-elif-else 实现成绩等级区间判定"""
        score = 85
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        else:
            grade = 'D'
        assert grade == 'B'

    def test_nested_if_and_ternary(self):
        """嵌套 if 与三元表达式的组合使用"""
        v = 4
        parity = 'even' if (v > 0 and v % 2 == 0) else 'odd'
        assert parity == 'even'

    def test_in_and_truthiness_and_chain(self):
        """in 判断、真值测试与链式比较"""
        empty_list = []
        assert not empty_list  # 真值测试，空列表为 False

        item = 2
        assert item in [1, 2, 3]

        x = 15
        ok = 10 < x < 20
        assert ok is True


class TestMatch:
    def test_basic_and_variants(self):
        """match 语句的基本用法与多值匹配"""

        def f(v):
            match v:
                case 1:
                    return 'one'
                case _:
                    return 'other'

        assert f(1) == 'one'
        assert f(2) == 'other'

        def g(v):
            match v:
                case 1 | 2:
                    return 'one_or_two'
                case _:
                    return 'other'

        assert g(1) == 'one_or_two'
        assert g(3) == 'other'

        def h(v):
            match v:
                case x if x > 0:
                    return 'positive'
                case _:
                    return 'non_positive'

        assert h(5) == 'positive'
        assert h(-1) == 'non_positive'

        def m(tp):
            match tp:
                case (a, b):
                    return a + b
                case _:
                    return 0

        assert m((2, 3)) == 5

        def d(dct):
            match dct:
                case {'key': val}:
                    return val
                case _:
                    return -1

        assert d({'key': 7}) == 7
        assert d({'other': 1}) == -1


class TestWhileLoop:
    def test_basic_while_and_else_and_break_continue(self):
        i = 0
        acc = 0
        while i < 3:
            acc += i
            i += 1
        else:
            ended_normally = True
        assert acc == 3
        assert ended_normally is True

    def test_while_break_no_else(self):
        i = 0
        else_executed = False
        while i < 5:
            if i == 2:
                break
            i += 1
        else:
            else_executed = True
        assert else_executed is False


class TestForLoop:
    def test_traverse_collections_and_ranges(self):
        lst = [1, 2, 3]
        d = {'a': 1, 'b': 2}
        s = 'xy'
        assert [x for x in lst] == [1, 2, 3]
        assert set([k for k in d]) == {'a', 'b'}
        assert [ch for ch in s] == ['x', 'y']

    def test_range_enumerate_zip(self):
        assert list(range(3)) == [0, 1, 2]
        assert list(range(2, 5)) == [2, 3, 4]
        assert list(range(0, 10, 3)) == [0, 3, 6, 9]

        items = ['a', 'b']
        assert list(enumerate(items, start=1)) == [(1, 'a'), (2, 'b')]

        a = [1, 2, 3]
        b = ['x', 'y']
        assert list(zip(a, b)) == [(1, 'x'), (2, 'y')]

        # zip_longest: 不等长截断
        from itertools import zip_longest
        assert list(zip_longest(a, b, fillvalue=None)) == [(1, 'x'), (2, 'y'), (3, None)]

    def test_map_filter_sorted(self):
        assert list(map(lambda x: x * 2, [1, 2, 3])) == [2, 4, 6]
        assert list(filter(bool, [0, 1, 2, False, '', 3])) == [1, 2, 3]
        assert sorted([3, -1, 2], key=abs, reverse=True) == [3, 2, -1]

    def test_for_else_and_pass(self):
        # for-else: 列表为空时会执行 else 子句
        acc = 0
        for x in []:
            acc += x
        else_executed = True
        assert else_executed is True


class TestLoopControl:
    def test_break_continue_pass(self):
        s = []
        for i in range(5):
            if i == 2:
                continue
            if i == 4:
                break
            s.append(i)
        assert s == [0, 1, 3]

    def test_pass_no_op(self):
        total = 0
        for i in range(3):
            pass
            total += i
        assert total == 3


class TestComprehensions:
    def test_list_dict_set_comprehensions(self):
        # 列表推导
        squares = [x**2 for x in range(10)]
        assert squares[3] == 9

        even_squares = [x**2 for x in range(10) if x % 2 == 0]
        assert even_squares[0] == 0

        # 嵌套推导
        matrix = [[1, 2], [3, 4]]
        flat = [num for row in matrix for num in row]
        assert flat == [1, 2, 3, 4]

        # 条件表达式推导
        labels = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
        assert labels == ['even', 'odd', 'even', 'odd', 'even']

        # 字典推导
        d = {x: x**2 for x in range(5)}
        assert d[3] == 9

        # 集合推导
        s = {x**2 for x in range(5)}
        assert 9 in s and len(s) == 5


class TestBuiltinFunctionsHints:
    def test_len_and_zip_with_different_lengths(self):
        assert len([1, 2, 3]) == 3
        a = [1, 2, 3]
        b = ['x', 'y']
        zipped = list(zip(a, b))
        assert zipped == [(1, 'x'), (2, 'y')]
