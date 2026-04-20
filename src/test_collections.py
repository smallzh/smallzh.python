#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""测试 Collections 模块的核心知识点
覆盖 Counter、DefaultDict、OrderedDict、Deque、NamedTuple、ChainMap、UserDict 等用法。"""

from __future__ import annotations

from collections import (
    Counter,
    defaultdict,
    OrderedDict,
    deque,
    namedtuple,
    ChainMap,
    UserDict,
)
from math import inf


def test_counter_basic_and_operations():
    """Counter 的创建方式、访问、most_common、elements、total、算术运算以及 update/subtract"""
    c = Counter("abracadabra")
    assert c['a'] == 5
    assert c['x'] == 0
    # most_common
    mc = c.most_common(2)
    assert mc[0][0] == 'a' and mc[0][1] == 5
    # total / elements / arithmetic
    total = c.total()
    assert total == 11
    # elements 的数量等于 total
    assert len(list(c.elements())) == total

    c2 = Counter({'a': 1, 'b': 3})
    c3 = c + c2
    assert c3['a'] == 6
    c4 = c - c2
    assert c4['a'] == 4
    # and/intersection
    c_and = c & Counter({'a': 1})
    assert c_and['a'] == 1
    # update / subtract
    c.update({'a': 1})
    assert c['a'] == 6
    c.subtract({'a': 1})
    assert c['a'] == 5


def test_defaultdict_behaviors():
    """defaultdict 的默认工厂行为：list、int、set、函数等"""
    d = defaultdict(list)
    d['x'].append(1)
    assert d['x'] == [1]

    d2 = defaultdict(int)
    d2['k'] += 2
    assert d2['k'] == 2

    # 自定义工厂函数
    d3 = defaultdict(lambda: 'missing')
    assert d3['not_exist'] == 'missing'


def test_group_by_using_defaultdict_and_adj_list():
    """分组应用与邻接表的简单构建"""
    data = [('a', 1), ('b', 2), ('a', 3)]
    groups = defaultdict(list)
    for k, v in data:
        groups[k].append(v)
    assert sorted(groups['a']) == [1, 3]
    # 邻接表
    edges = [('A', 'B'), ('A', 'C'), ('B', 'C')]
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
    assert adj['A'] == ['B', 'C']


def test_ordered_dict_behaviors():
    """有序字典保持插入顺序，支持 move_to_end 和 popitem"""
    od = OrderedDict()
    od['one'] = 1
    od['two'] = 2
    assert list(od.keys()) == ['one', 'two']
    od.move_to_end('one')
    assert list(od.keys()) == ['two', 'one']
    k, v = od.popitem(last=True)
    assert (k, v) == ('one', 1)
    # last=False
    od2 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    first = od2.popitem(last=False)
    assert first == ('a', 1)


def test_namedtuple_behaviors():
    """命名元组的创建、属性访问、索引访问、解包、_asdict、_replace、_fields"""
    Pt = namedtuple('Pt', ['x', 'y'])
    p = Pt(1, 2)
    assert p.x == 1
    assert p[0] == 1
    d = p._asdict()
    assert d['x'] == 1
    p2 = p._replace(y=5)
    assert p2.y == 5
    assert Pt._fields == ('x', 'y')


def test_chainmap_behaviors():
    d1 = {'a': 1}
    d2 = {'b': 2}
    cm = ChainMap(d1, d2)
    assert cm['a'] == 1
    assert cm['b'] == 2
    new = cm.new_child()
    new['c'] = 3
    assert new['c'] == 3


def test_userdict_and_misc_wrappers():
    """使用 UserDict 演示简单的包装，而非引入第三方库"""
    class CaseInsensitiveDict(UserDict):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def __setitem__(self, key, value):
            super().__setitem__(str(key).lower(), value)

        def __getitem__(self, key):
            return super().__getitem__(str(key).lower())

    cid = CaseInsensitiveDict()
    cid['Apple'] = 5
    assert cid['apple'] == 5

    # 简单的 SortedList 实现，使用 bisect 插入，测试排序效果
    from bisect import insort

    class SortedList(list):
        def add(self, value):
            insort(self, value)

    sl = SortedList()
    sl.add(3)
    sl.add(1)
    sl.add(2)
    assert sl == [1, 2, 3]

    # UpperString 继承自 str，自动转为大写
    class UpperString(str):
        def __new__(cls, value):
            return str.__new__(cls, value.upper())

    us = UpperString('abc')
    assert isinstance(us, str) and us == 'ABC'
