# 一切皆对象

在 Python 中，一切皆是对象（Everything is Object）。这是 Python 最核心的设计哲学之一。

## 0x01. 对象的本质

### 对象的三要素

每个 Python 对象都包含三个基本要素：

```python
"""
- Identity（标识）：对象的唯一标识，通常是内存地址
- Type（类型）：决定对象有哪些操作和能存储什么值
- Value（值）：对象存储的数据
"""

# 示例
num = 42

# 获取对象的标识（内存地址）
print(id(num))  # 例如: 140234567890

# 获取对象的类型
print(type(num))  # <class 'int'>

# 获取对象的值
print(num)  # 42
```

### Everything is Object

```python
# 数字是对象
num = 42
print(type(num))  # <class 'int'>

# 字符串是对象
text = "hello"
print(type(text))  # <class 'str'>

# 列表是对象
lst = [1, 2, 3]
print(type(lst))  # <class 'list'>

# 函数是对象
def func():
    pass
print(type(func))  # <class 'function'>

# 类是对象
class MyClass:
    pass
print(type(MyClass))  # <class 'type'>

# 模块是对象
import sys
print(type(sys))  # <class 'module'>

# 甚至 type 本身也是对象
print(type(type))  # <class 'type'>

# None 是对象
print(type(None))  # <class 'NoneType'>
```

## 0x02. 引用与赋值

### 变量是引用

```python
# 在 Python 中，变量不是存储容器，而是对象的引用（标签）

# 示例 1：多个变量引用同一对象
a = [1, 2, 3]
b = a  # b 和 a 引用同一个列表对象

print(id(a) == id(b))  # True - 相同的内存地址
print(a is b)          # True - 是同一个对象

# 修改 a 会影响 b
a.append(4)
print(b)  # [1, 2, 3, 4]

# 示例 2：整数的引用
x = 100
y = 100
print(x is y)  # True - Python 缓存了小整数 (-5 到 256)

# 但大整数可能不同
a = 1000
b = 1000
print(a is b)  # 可能是 False（取决于实现）
print(a == b)  # True - 值相等
```

### 赋值的本质

```python
# 赋值操作是创建新的引用，不是复制对象

# 示例 1：不可变对象的赋值
a = 10
b = a
b = 20  # 这里创建了新的整数对象 20，让 b 引用它
print(a)  # 10 - a 仍然引用原来的对象

# 示例 2：可变对象的赋值
a = [1, 2, 3]
b = a
b[0] = 999  # 修改的是同一个列表对象
print(a)  # [999, 2, 3]

# 示例 3：重新赋值 vs 修改
a = [1, 2, 3]
b = a
b = [4, 5, 6]  # b 引用新的列表对象，a 不受影响
print(a)  # [1, 2, 3]
```

## 0x03. 可变性与不可变性

### 不可变对象（Immutable）

```python
"""
不可变对象创建后不能被修改：
- int, float, complex
- str
- tuple
- frozenset
- bytes
"""

# 不可变对象的"修改"实际上是创建新对象
s = "hello"
print(id(s))  # 原始地址

s = s + " world"  # 创建新的字符串对象
print(id(s))  # 不同的地址

# 元组包含可变对象时的陷阱
t = ([1, 2], [3, 4])
# t[0] = [5, 6]  # TypeError: 元组不能修改
t[0].append(3)   # 但元组内的列表可以修改
print(t)  # ([1, 2, 3], [3, 4])
```

### 可变对象（Mutable）

```python
"""
可变对象可以被原地修改：
- list
- dict
- set
- bytearray
- 自定义类实例（默认）
"""

# 可变对象可以原地修改，地址不变
lst = [1, 2, 3]
print(id(lst))  # 原始地址

lst.append(4)   # 原地修改
print(id(lst))  # 相同的地址

# 字典的原地修改
d = {'a': 1}
print(id(d))

d['b'] = 2
print(id(d))  # 相同的地址
```

### 可变性的影响

```python
# 1. 作为字典键
# 不可变对象可以作为字典键
d = {}
d[1] = 'int'
d['str'] = 'string'
d[(1, 2)] = 'tuple'

# 可变对象不能作为字典键
# d[[1, 2]] = 'list'  # TypeError: unhashable type: 'list'

# 2. 函数参数传递
def modify_list(lst):
    lst.append(4)  # 会影响原列表

def modify_int(n):
    n += 1  # 不会影响原整数

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 4]

my_int = 10
modify_int(my_int)
print(my_int)  # 10
```

## 0x04. 对象的比较

### == 与 is

```python
"""
== 比较值是否相等
is 比较是否是同一个对象（内存地址相同）
"""

# 示例 1：列表比较
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True - 值相等
print(a is b)  # False - 不是同一个对象
print(a is c)  # True - 是同一个对象

# 示例 2：None 的比较
x = None
# 推荐使用 is 比较 None
if x is None:
    print('x is None')

# 不推荐
if x == None:
    print('x is None')
```

### Python 的对象缓存

```python
# 小整数缓存 (-5 到 256)
a = 100
b = 100
print(a is b)  # True

a = 300
b = 300
print(a is b)  # 可能是 False

# 字符串驻留（interning）
s1 = 'hello'
s2 = 'hello'
print(s1 is s2)  # True - 短字符串会被驻留

s1 = 'hello world!'
s2 = 'hello world!'
print(s1 is s2)  # 可能是 False
```

## 0x05. 特殊方法（魔术方法）

### 对象的生命周期

```python
class MyClass:
    def __new__(cls, *args, **kwargs):
        """创建对象实例（在 __init__ 之前调用）"""
        print('__new__ 被调用')
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, value):
        """初始化对象"""
        print('__init__ 被调用')
        self.value = value
    
    def __del__(self):
        """对象被销毁时调用"""
        print(f'{self} 被销毁')

obj = MyClass(42)
# __new__ 被调用
# __init__ 被调用

del obj
# <__main__.MyClass object at 0x...> 被销毁
```

### 字符串表示

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        """官方字符串表示，用于调试"""
        return f'Point({self.x}, {self.y})'
    
    def __str__(self):
        """用户友好的字符串表示"""
        return f'({self.x}, {self.y})'
    
    def __format__(self, format_spec):
        """格式化输出"""
        if format_spec == 'c':  # 坐标格式
            return f'({self.x}, {self.y})'
        return str(self)

p = Point(3, 4)
print(repr(p))   # Point(3, 4)
print(str(p))    # (3, 4)
print(f'{p:c}')  # (3, 4)
```

### 比较运算符

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        """== 运算符"""
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        """< 运算符"""
        return (self.x, self.y) < (other.x, other.y)
    
    def __le__(self, other):
        """<= 运算符"""
        return self < other or self == other
    
    def __hash__(self):
        """哈希值，使对象可用作字典键"""
        return hash((self.x, self.y))

v1 = Vector(1, 2)
v2 = Vector(1, 2)
v3 = Vector(3, 4)

print(v1 == v2)  # True
print(v1 < v3)   # True
```

### 算术运算符

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """+ 运算符"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """- 运算符"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """* 运算符（标量乘法）"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):
        """反向乘法：scalar * vector"""
        return self.__mul__(scalar)
    
    def __neg__(self):
        """- 取负运算符"""
        return Vector(-self.x, -self.y)
    
    def __abs__(self):
        """abs() 函数"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2
print(v3.x, v3.y)  # 4 6

v4 = v1 * 2
print(v4.x, v4.y)  # 2 4

v5 = 2 * v1  # 调用 __rmul__
print(v5.x, v5.y)  # 2 4
```

### 容器协议

```python
class CustomList:
    def __init__(self, *items):
        self._items = list(items)
    
    def __len__(self):
        """len() 函数"""
        return len(self._items)
    
    def __getitem__(self, index):
        """索引访问：obj[index]"""
        return self._items[index]
    
    def __setitem__(self, index, value):
        """索引赋值：obj[index] = value"""
        self._items[index] = value
    
    def __delitem__(self, index):
        """删除元素：del obj[index]"""
        del self._items[index]
    
    def __contains__(self, item):
        """in 运算符"""
        return item in self._items
    
    def __iter__(self):
        """迭代器"""
        return iter(self._items)
    
    def __reversed__(self):
        """reversed() 函数"""
        return reversed(self._items)

cl = CustomList(1, 2, 3, 4, 5)
print(len(cl))      # 5
print(cl[0])        # 1
print(3 in cl)      # True
for item in cl:
    print(item)
```

### 可调用对象

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        """使对象可以像函数一样调用"""
        return x * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15

# 检查对象是否可调用
print(callable(double))  # True
```

### 上下文管理器

```python
class Timer:
    def __enter__(self):
        """进入 with 块时调用"""
        import time
        self.start = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出 with 块时调用"""
        import time
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        print(f'耗时: {self.elapsed:.4f} 秒')
        return False  # 不抑制异常

with Timer() as timer:
    sum(range(1000000))
# 耗时: 0.0321 秒
```

## 0x06. 类型系统

### 类型层级

```python
# 所有类最终继承自 object
print(int.__bases__)       # (<class 'object'>,)
print(str.__bases__)       # (<class 'object'>,)
print(list.__bases__)      # (<class 'object'>,)

# type 是所有类的元类
print(type(int))           # <class 'type'>
print(type(str))           # <class 'type'>
print(type(object))        # <class 'type'>

# type 本身也是 type
print(type(type))          # <class 'type'>

# isinstance 检查
print(isinstance(42, int))        # True
print(isinstance(42, object))     # True
print(isinstance(int, type))      # True
print(isinstance(object, type))   # True
```

### 动态创建类

```python
# 使用 type 动态创建类
# type(name, bases, attrs)
MyClass = type('MyClass', (object,), {
    'x': 42,
    'hello': lambda self: 'Hello!'
})

obj = MyClass()
print(obj.x)         # 42
print(obj.hello())   # Hello!
print(type(obj))     # <class '__main__.MyClass'>

# 等价于
class MyClass:
    x = 42
    def hello(self):
        return 'Hello!'
```

## 0x07. 实际应用

### 对象的深浅拷贝

```python
import copy

# 原始对象
original = [[1, 2], [3, 4]]

# 浅拷贝：只复制第一层
shallow = copy.copy(original)
shallow[0][0] = 999
print(original)  # [[999, 2], [3, 4]] - 原对象被影响

# 深拷贝：递归复制所有层
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 999
print(original)  # [[1, 2], [3, 4]] - 原对象不受影响
```

### 实现自定义容器

```python
from collections.abc import MutableSequence

class SortedList(MutableSequence):
    """自动排序的列表"""
    
    def __init__(self, iterable=None):
        self._data = []
        if iterable:
            self.extend(iterable)
    
    def __repr__(self):
        return f'SortedList({self._data})'
    
    def __len__(self):
        return len(self._data)
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __setitem__(self, index, value):
        del self._data[index]
        self._data.insert(self._bisect_left(value), value)
    
    def __delitem__(self, index):
        del self._data[index]
    
    def insert(self, index, value):
        """插入并保持排序"""
        self._data.insert(self._bisect_left(value), value)
    
    def _bisect_left(self, value):
        """二分查找插入位置"""
        lo, hi = 0, len(self._data)
        while lo < hi:
            mid = (lo + hi) // 2
            if self._data[mid] < value:
                lo = mid + 1
            else:
                hi = mid
        return lo

# 使用
sl = SortedList([3, 1, 4, 1, 5, 9, 2, 6])
print(sl)  # SortedList([1, 1, 2, 3, 4, 5, 6, 9])

sl.append(0)
print(sl)  # SortedList([0, 1, 1, 2, 3, 4, 5, 6, 9])
```

### 对象属性访问控制

```python
class ProtectedObject:
    def __init__(self):
        self._data = {}
    
    def __getattr__(self, name):
        """访问不存在的属性时调用"""
        print(f'__getattr__: {name}')
        return self._data.get(name, None)
    
    def __setattr__(self, name, value):
        """设置属性时调用"""
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print(f'__setattr__: {name} = {value}')
            self._data[name] = value
    
    def __delattr__(self, name):
        """删除属性时调用"""
        print(f'__delattr__: {name}')
        del self._data[name]

obj = ProtectedObject()
obj.name = 'Alice'  # __setattr__: name = Alice
print(obj.name)     # __getattr__: name \n Alice
del obj.name        # __delattr__: name
```

## 参考
1. [Python 官方文档 - 数据模型](https://docs.python.org/3/reference/datamodel.html)
2. [Python 官方文档 - 内置类型](https://docs.python.org/3/library/stdtypes.html)
3. [Python 官方文档 - 特殊方法](https://docs.python.org/3/reference/datamodel.html#special-method-names)
4. [Fluent Python - Luciano Ramalho](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)