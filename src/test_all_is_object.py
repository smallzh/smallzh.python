"""测试：all is object 系列知识点的 pytest 风格用例"""
import types
import copy


def test_object_identity():
    """TestObjectIdentity：对象的三要素演示（id、type、值）"""
    x = 123
    assert id(x) >= 0
    assert type(x) is int
    assert x == 123


def test_everything_is_object():
    """TestEverythingIsObject：一切皆对象的基本断言"""
    assert type(42) is int
    assert type("hello") is str
    assert type([1, 2, 3]) is list
    def f():
        pass
    assert type(f) is types.FunctionType
    class MyClass:  # simple class
        pass
    assert type(MyClass) is type
    import math
    assert type(math) is types.ModuleType
    assert type(type) is type


def test_reference_assignment():
    a = []
    b = a
    a.append(1)
    assert b is a
    assert b == [1]
    a = [2]
    assert b is not a


def test_immutability():
    s = "hello"
    id_before = id(s)
    s = s + " world"
    assert id(s) != id_before
    # 元组不可变，但元组内元素可变时可以修改其中元素
    inner = ([1, 2],)
    tup = (inner,)
    inner[0].append(3)
    assert tup[0][0] == [1, 2, 3]


def test_mutability():
    lst = [1, 2, 3]
    orig_id = id(lst)
    lst.append(4)
    assert id(lst) == orig_id
    d = {"a": 1}
    orig_id_d = id(d)
    d["b"] = 2
    assert id(d) == orig_id_d


def test_comparison():
    a = [1, 2]
    b = [1, 2]
    assert a == b
    assert a is not b
    x = None
    assert x is None
    # 小整数缓存
    c1 = 256
    c2 = 256
    assert c1 is c2
    # 字符串驻留（可能受实现影响，此断言尽量稳健）
    s1 = "interned"
    s2 = "interned"
    # 许多实现会将短字符串驻留，使其同一对象
    assert (s1 == s2)


def test_deep_shallow_copy():
    import copy
    data = [1, [2, 3]]
    shallow = copy.copy(data)
    deep = copy.deepcopy(data)
    # 浅拷贝：嵌套对象引用共享
    shallow[1].append(4)
    assert data[1] == [2, 3, 4]
    # 深拷贝：嵌套对象独立
    assert deep[1] == [2, 3]


def test_magic_methods():
    class Container:
        def __init__(self, items=None):
            self._items = list(items or [])
        def __repr__(self):
            return f"Container({self._items!r})"
        def __str__(self):
            return f"Container with {len(self._items)} items"
        def __len__(self):
            return len(self._items)
        def __getitem__(self, idx):
            return self._items[idx]
        def __setitem__(self, idx, val):
            self._items[idx] = val
        def __iter__(self):
            return iter(self._items)
        def __contains__(self, item):
            return item in self._items
        def __add__(self, other):
            if isinstance(other, Container):
                return Container(self._items + other._items)
            return NotImplemented
    c1 = Container([1, 2, 3])
    c2 = Container([4, 5])
    c3 = c1 + c2
    assert isinstance(c3, Container) and list(c3) == [1, 2, 3, 4, 5]
    assert len(c1) == 3
    assert c1[0] == 1
    c1[0] = 9
    assert c1[0] == 9
    assert 2 in c1
    assert repr(c1).startswith("Container(")
    # 使对象可调用
    class Callable:
        def __init__(self, v):
            self.v = v
        def __call__(self, x):
            return self.v + x
    f = Callable(5)
    assert callable(f) and f(3) == 8


def test_type_system():
    class A: pass
    class B(A): pass
    assert B.__bases__[0] is A
    assert isinstance(3, object)
    assert isinstance(int, type)
    C = type("Dynamic", (object,), {})
    assert isinstance(C(), object)
