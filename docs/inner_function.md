# 内部函数

Python 提供了许多内置函数，这些函数可以直接使用，无需导入任何模块。

## 0x01. 类型转换函数

### int()

```python
# 字符串转整数
print(int('42'))        # 42
print(int('0b1010', 2)) # 10 (二进制)
print(int('0o12', 8))   # 10 (八进制)
print(int('0xa', 16))   # 10 (十六进制)

# 浮点数转整数（向下取整）
print(int(3.14))        # 3
print(int(-3.14))       # -3

# 布尔值转整数
print(int(True))        # 1
print(int(False))       # 0
```

### float()

```python
# 字符串转浮点数
print(float('3.14'))    # 3.14
print(float('1e-3'))    # 0.001

# 整数转浮点数
print(float(42))        # 42.0

# 布尔值转浮点数
print(float(True))      # 1.0
```

### str()

```python
# 其他类型转字符串
print(str(42))          # '42'
print(str(3.14))        # '3.14'
print(str(True))        # 'True'
print(str([1, 2, 3]))   # '[1, 2, 3]'
```

### bool()

```python
# 真值测试
print(bool(0))          # False
print(bool(1))          # True
print(bool(''))         # False
print(bool('hello'))    # True
print(bool([]))         # False
print(bool([1, 2]))     # True
print(bool(None))       # False
```

### list()

```python
# 其他可迭代对象转列表
print(list('hello'))    # ['h', 'e', 'l', 'l', 'o']
print(list((1, 2, 3)))  # [1, 2, 3]
print(list({1, 2, 3}))  # [1, 2, 3]
print(list({'a': 1, 'b': 2}))  # ['a', 'b']
print(list(range(5)))   # [0, 1, 2, 3, 4]

# 创建空列表
empty = list()
print(empty)            # []
```

### tuple()

```python
# 其他可迭代对象转元组
print(tuple([1, 2, 3])) # (1, 2, 3)
print(tuple('hello'))   # ('h', 'e', 'l', 'l', 'o')
print(tuple(range(5)))  # (0, 1, 2, 3, 4)
```

### set()

```python
# 其他可迭代对象转集合（去重）
print(set([1, 2, 2, 3, 3, 3]))  # {1, 2, 3}
print(set('hello'))              # {'h', 'e', 'l', 'o'}
print(set({'a': 1, 'b': 2}))    # {'a', 'b'}
```

### dict()

```python
# 从键值对创建字典
print(dict([('a', 1), ('b', 2)]))  # {'a': 1, 'b': 2}
print(dict(a=1, b=2))              # {'a': 1, 'b': 2}
print(dict.fromkeys(['a', 'b'], 0)) # {'a': 0, 'b': 0}
```

## 0x02. 数学函数

### abs()

```python
# 返回绝对值
print(abs(-42))         # 42
print(abs(3.14))        # 3.14
print(abs(-3 + 4j))     # 5.0 (复数的模)
```

### round()

```python
# 四舍五入
print(round(3.14))      # 3
print(round(3.5))       # 4
print(round(3.14159, 2)) # 3.14
print(round(3.14159, 4)) # 3.1416

# 银行家舍入法（四舍六入五成双）
print(round(0.5))       # 0
print(round(1.5))       # 2
print(round(2.5))       # 2
```

### pow()

```python
# 幂运算
print(pow(2, 3))        # 8
print(pow(2, 3, 5))     # 3 (2^3 % 5)

# 等价于 ** 运算符
print(2 ** 3)           # 8
```

### divmod()

```python
# 同时返回商和余数
print(divmod(10, 3))    # (3, 1)
print(divmod(9, 3))     # (3, 0)

# 等价于
a, b = 10, 3
print((a // b, a % b))  # (3, 1)
```

### sum()

```python
# 求和
print(sum([1, 2, 3, 4, 5]))  # 15
print(sum([1, 2, 3], 10))    # 16 (带初始值)
print(sum((x**2 for x in range(5))))  # 30 (生成器表达式)
```

### min() 和 max()

```python
# 最小值和最大值
print(min([3, 1, 4, 1, 5]))  # 1
print(max([3, 1, 4, 1, 5]))  # 5

# 多个参数
print(min(3, 1, 4, 1, 5))    # 1
print(max(3, 1, 4, 1, 5))    # 5

# 使用 key 函数
print(min(['banana', 'apple', 'cherry'], key=len))  # 'apple'
print(max(['banana', 'apple', 'cherry'], key=len))  # 'banana'
```

## 0x03. 序列操作函数

### len()

```python
# 返回长度
print(len([1, 2, 3]))       # 3
print(len('hello'))         # 5
print(len({'a': 1, 'b': 2})) # 2
print(len({1, 2, 3}))       # 3
print(len(range(10)))       # 10
```

### range()

```python
# 生成数字序列
print(list(range(5)))         # [0, 1, 2, 3, 4]
print(list(range(2, 7)))      # [2, 3, 4, 5, 6]
print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]
print(list(range(10, 0, -2))) # [10, 8, 6, 4, 2]
```

### sorted()

```python
# 排序（返回新列表）
print(sorted([3, 1, 4, 1, 5]))  # [1, 1, 3, 4, 5]
print(sorted([3, 1, 4, 1, 5], reverse=True))  # [5, 4, 3, 1, 1]

# 使用 key 函数
words = ['banana', 'Apple', 'cherry']
print(sorted(words))              # ['Apple', 'banana', 'cherry']
print(sorted(words, key=str.lower))  # ['Apple', 'banana', 'cherry']

# 复杂排序
students = [
    {'name': 'Alice', 'grade': 88},
    {'name': 'Bob', 'grade': 95},
    {'name': 'Charlie', 'grade': 82}
]
print(sorted(students, key=lambda x: x['grade'], reverse=True))
```

### reversed()

```python
# 反转序列
print(list(reversed([1, 2, 3, 4, 5])))  # [5, 4, 3, 2, 1]
print(list(reversed('hello')))           # ['o', 'l', 'l', 'e', 'h']

# 在循环中使用
for i in reversed(range(5)):
    print(i)
# 4 3 2 1 0
```

### enumerate()

```python
# 带索引遍历
fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    print(f'{i}: {fruit}')
# 0: apple
# 1: banana
# 2: cherry

# 指定起始索引
for i, fruit in enumerate(fruits, 1):
    print(f'{i}: {fruit}')
# 1: apple
# 2: banana
# 3: cherry
```

### zip()

```python
# 并行遍历多个序列
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f'{name}: {age}')
# Alice: 25
# Bob: 30
# Charlie: 35

# 不等长序列
a = [1, 2, 3]
b = ['a', 'b']
print(list(zip(a, b)))  # [(1, 'a'), (2, 'b')]

# 使用 zip_longest 处理不等长
from itertools import zip_longest
print(list(zip_longest(a, b, fillvalue='?')))  # [(1, 'a'), (2, 'b'), (3, '?')]
```

### map()

```python
# 对序列中的每个元素应用函数
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# 多个序列
a = [1, 2, 3]
b = [4, 5, 6]
sums = list(map(lambda x, y: x + y, a, b))
print(sums)  # [5, 7, 9]

# 使用内置函数
words = ['hello', 'world', 'python']
lengths = list(map(len, words))
print(lengths)  # [5, 5, 6]
```

### filter()

```python
# 过滤序列
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# 使用 None 过滤假值
values = [0, 1, False, True, '', 'hello', None]
truthy = list(filter(None, values))
print(truthy)  # [1, True, 'hello']
```

## 0x04. 输入输出函数

### print()

```python
# 基本输出
print('Hello, World!')

# 输出多个值
print('Hello', 'World', 'Python')  # Hello World Python

# 指定分隔符
print('a', 'b', 'c', sep='-')      # a-b-c

# 指定结尾符
print('Hello', end=' ')
print('World')  # Hello World

# 输出到文件
with open('output.txt', 'w') as f:
    print('Hello, File!', file=f)
```

### input()

```python
# 获取用户输入
name = input('请输入你的名字: ')
print(f'你好, {name}!')

# 输入总是返回字符串
age = input('请输入你的年龄: ')
age = int(age)  # 需要类型转换

# 在一行中获取多个值
x, y = input('输入两个数字，用空格分隔: ').split()
x, y = int(x), int(y)
```

### open()

```python
# 打开文件
# 详见 file.md 文档
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
```

## 0x05. 对象操作函数

### type()

```python
# 获取类型
print(type(42))         # <class 'int'>
print(type('hello'))    # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>

# 动态创建类
MyClass = type('MyClass', (), {'x': 42})
obj = MyClass()
print(obj.x)  # 42
```

### isinstance()

```python
# 类型检查
print(isinstance(42, int))          # True
print(isinstance('hello', str))     # True
print(isinstance(42, (int, float))) # True (检查多个类型)
```

### id()

```python
# 获取对象的唯一标识（通常是内存地址）
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(id(a))          # 140234567890 (示例)
print(id(b))          # 140234567890 (相同)
print(id(c))          # 140234567891 (不同)
print(a is b)         # True
print(a is c)         # False
```

### hash()

```python
# 获取对象的哈希值（用于字典和集合）
print(hash('hello'))    # 示例: -1234567890
print(hash(42))         # 42
print(hash((1, 2, 3)))  # 示例: 529344067295497451

# 可哈希对象：不可变类型（int, str, tuple, frozenset）
# 不可哈希对象：可变类型（list, dict, set）
# hash([1, 2, 3])  # TypeError: unhashable type: 'list'
```

### hasattr() 和 getattr()

```python
class MyClass:
    x = 42

obj = MyClass()

# 检查属性是否存在
print(hasattr(obj, 'x'))    # True
print(hasattr(obj, 'y'))    # False

# 获取属性值
print(getattr(obj, 'x'))    # 42
print(getattr(obj, 'y', 0)) # 0 (默认值)

# 设置属性
setattr(obj, 'y', 100)
print(obj.y)  # 100

# 删除属性
delattr(obj, 'y')
print(hasattr(obj, 'y'))  # False
```

### callable()

```python
# 检查对象是否可调用
print(callable(print))      # True
print(callable(len))        # True
print(callable(lambda x: x)) # True

def func():
    pass

print(callable(func))       # True
print(callable(42))         # False
```

## 0x06. 字符相关函数

### chr() 和 ord()

```python
# Unicode 码点与字符转换
print(ord('A'))     # 65
print(ord('中'))    # 20013
print(chr(65))      # 'A'
print(chr(20013))   # '中'

# ASCII 范围
print(ord('a'))     # 97
print(ord('z'))     # 122
print(ord('0'))     # 48
print(ord('9'))     # 57
```

### repr()

```python
# 返回对象的官方字符串表示
print(repr('hello'))      # "'hello'"
print(repr([1, 2, 3]))    # '[1, 2, 3]'
print(repr(3.14))         # '3.14'

# 自定义 repr
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Point({self.x}, {self.y})'

p = Point(3, 4)
print(repr(p))  # 'Point(3, 4)'
```

### ascii()

```python
# 类似 repr()，但非 ASCII 字符会被转义
print(ascii('你好'))      # '\\u4f60\\u597d'
print(ascii('hello'))     # "'hello'"
```

## 0x07. 迭代器操作函数

### iter() 和 next()

```python
# 获取迭代器
it = iter([1, 2, 3])
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # StopIteration

# 带默认值的 next
it = iter([1, 2, 3])
print(next(it, 'end'))  # 1
print(next(it, 'end'))  # 2
print(next(it, 'end'))  # 3
print(next(it, 'end'))  # 'end'
```

### all() 和 any()

```python
# all()：所有元素都为 True 则返回 True
print(all([True, True, True]))   # True
print(all([True, False, True]))  # False
print(all([1, 2, 3]))            # True
print(all([1, 0, 3]))            # False
print(all([]))                   # True (空列表)

# any()：任意元素为 True 则返回 True
print(any([False, False, False])) # False
print(any([False, True, False]))  # True
print(any([0, 0, 1]))            # True
print(any([0, 0, 0]))            # False
print(any([]))                   # False (空列表)
```

## 0x08. 其他实用函数

### vars()

```python
# 返回对象的 __dict__ 属性
class MyClass:
    x = 42
    y = 'hello'

print(vars(MyClass))  # {'x': 42, 'y': 'hello', ...}

obj = MyClass()
obj.z = 100
print(vars(obj))  # {'z': 100}

# 无参数时返回局部变量
def func():
    x = 1
    y = 2
    print(vars())

func()  # {'x': 1, 'y': 2}
```

### dir()

```python
# 返回对象的属性和方法列表
print(dir([]))  # 列表的所有方法

# 查看模块内容
import os
print(dir(os))
```

### help()

```python
# 查看帮助信息
help(list)
help(list.append)
```

### globals() 和 locals()

```python
# 返回全局和局部符号表
x = 10
y = 20

def func():
    a = 1
    b = 2
    print(locals())  # {'a': 1, 'b': 2}

func()
print(globals())  # 包含 x, y 等全局变量
```

### breakpoint() (Python 3.7+)

```python
# 设置断点
def func():
    x = 10
    breakpoint()  # 进入调试器
    y = 20
    return x + y
```

## 参考
1. [Python 官方文档 - 内置函数](https://docs.python.org/3/library/functions.html)
2. [Python 内置函数速查表](https://docs.python.org/3/library/functions.html)