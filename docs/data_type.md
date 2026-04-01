# 支持哪些数据类型？

Python 中的数据类型分为以下几类：
1. 基本数据类型：数字、字符串、布尔值
2. 容器类型：列表、元组、字典、集合
3. 特殊类型：None、bytes、bytearray 等

## 0x01. 数字类型

### 整数 int
整数可以是正数或负数，没有小数部分。

```python
# 整数的多种进制表示
decimal_num = 42          # 十进制
binary_num = 0b1010       # 二进制，结果为 10
octal_num = 0o52          # 八进制，结果为 42
hex_num = 0x2A            # 十六进制，结果为 42

# 大整数可以用下划线分隔提高可读性
large_num = 1_000_000_000  # 十亿

print(decimal_num)         # 42
print(binary_num)          # 10
print(octal_num)           # 42
print(hex_num)             # 42
print(large_num)           # 1000000000
```

### 浮点数 float
浮点数包含小数部分，也可以用科学计数法表示。

```python
# 浮点数表示
pi = 3.14159
negative_float = -2.5
scientific = 1.5e10  # 科学计数法，1.5 × 10^10

print(pi)            # 3.14159
print(scientific)    # 15000000000.0

# 浮点数精度问题
result = 0.1 + 0.2
print(result)        # 0.30000000000000004
print(result == 0.3) # False

# 使用 round() 或 math.isclose() 处理精度
import math
print(math.isclose(0.1 + 0.2, 0.3))  # True
```

### 复数 complex
复数由实部和虚部组成。

```python
# 复数的创建方式
z1 = 3 + 4j
z2 = complex(3, 4)

print(z1)            # (3+4j)
print(z2.real)       # 3.0 (实部)
print(z2.imag)       # 4.0 (虚部)

# 复数运算
z3 = z1 + z2
print(z3)            # (6+8j)

# 取模
print(abs(z1))       # 5.0 (sqrt(3^2 + 4^2))
```

## 0x02. 布尔类型 bool

布尔类型只有两个值：`True` 和 `False`。

```python
# 布尔值
is_active = True
is_deleted = False

# 布尔运算
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# 真值测试：以下值在布尔上下文中为 False
print(bool(0))          # False
print(bool(0.0))        # False
print(bool(''))         # False (空字符串)
print(bool([]))         # False (空列表)
print(bool({}))         # False (空字典)
print(bool(None))       # False
print(bool(False))      # False

# 其他值通常为 True
print(bool(1))          # True
print(bool('hello'))    # True
print(bool([1, 2]))     # True
```

## 0x03. 字符串 str

字符串是不可变的字符序列。

```python
# 字符串的多种创建方式
s1 = 'hello'
s2 = "world"
s3 = '''多行
字符串'''
s4 = """另一个
多行字符串"""

# 原始字符串（不转义）
path = r'C:\Users\name'

# f-string 格式化
name = 'Alice'
age = 25
greeting = f'Hello, {name}! You are {age} years old.'
print(greeting)  # Hello, Alice! You are 25 years old.

# 字符串常用操作
s = 'hello world'
print(len(s))           # 11
print(s.upper())        # HELLO WORLD
print(s.lower())        # hello world
print(s.split(' '))     # ['hello', 'world']
print(' '.join(['a', 'b']))  # 'a b'
print(s.replace('hello', 'hi'))  # 'hi world'
print(s.strip())        # 去除首尾空白
```

## 0x04. 列表 list

列表是有序、可变的序列类型。

```python
# 创建列表
fruits = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3, 4, 5]
mixed = [1, 'hello', 3.14, True]  # 可以包含不同类型的元素

# 访问元素（索引从 0 开始）
print(fruits[0])        # 'apple'
print(fruits[-1])       # 'cherry' (最后一个元素)

# 修改元素
fruits[1] = 'blueberry'
print(fruits)           # ['apple', 'blueberry', 'cherry']

# 添加元素
fruits.append('date')   # 在末尾添加
fruits.insert(1, 'banana')  # 在指定位置插入
fruits.extend(['elderberry', 'fig'])  # 扩展列表

# 删除元素
fruits.remove('apple')  # 删除第一个匹配的元素
popped = fruits.pop()   # 删除并返回最后一个元素
del fruits[0]           # 删除指定索引的元素

# 列表切片
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])        # [1, 2, 3]
print(nums[::2])        # [0, 2, 4]
print(nums[::-1])       # [5, 4, 3, 2, 1, 0]

# 列表推导式
squares = [x**2 for x in range(10)]
print(squares)          # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 常用方法
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(len(nums))        # 8
print(min(nums))        # 1
print(max(nums))        # 9
print(sum(nums))        # 31
print(sorted(nums))     # [1, 1, 2, 3, 4, 5, 6, 9]
print(nums.count(1))    # 2 (出现次数)
print(nums.index(4))    # 2 (第一个匹配的索引)
```

## 0x05. 元组 tuple

元组是有序、不可变的序列类型。

```python
# 创建元组
coordinates = (10, 20)
single_tuple = (1,)  # 单元素元组需要逗号
empty_tuple = ()

# 访问元素
print(coordinates[0])   # 10
print(coordinates[-1])  # 20

# 元组解包
x, y = coordinates
print(x, y)             # 10 20

# 元组不可变，以下操作会报错
# coordinates[0] = 100  # TypeError

# 元组常用场景
# 1. 函数返回多个值
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()

# 2. 作为字典键（因为不可变）
locations = {(0, 0): 'origin', (1, 0): 'right'}
```

## 0x06. 字典 dict

字典是键值对的无序集合（Python 3.7+ 保持插入顺序）。

```python
# 创建字典
person = {
    'name': 'Alice',
    'age': 25,
    'city': 'Beijing'
}

# 访问值
print(person['name'])   # 'Alice'
print(person.get('email', 'not found'))  # 'not found' (键不存在时返回默认值)

# 添加/修改键值对
person['email'] = 'alice@example.com'
person['age'] = 26

# 删除键值对
del person['city']
email = person.pop('email')

# 字典遍历
for key in person:
    print(key)          # 遍历键

for value in person.values():
    print(value)        # 遍历值

for key, value in person.items():
    print(f'{key}: {value}')  # 遍历键值对

# 字典推导式
squares = {x: x**2 for x in range(5)}
print(squares)          # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 常用方法
print(person.keys())    # dict_keys([...])
print(person.values())  # dict_values([...])
print(person.items())   # dict_items([...])
print(len(person))      # 键值对数量

# 合并字典
defaults = {'theme': 'light', 'lang': 'en'}
user_prefs = {'theme': 'dark'}
merged = {**defaults, **user_prefs}
print(merged)           # {'theme': 'dark', 'lang': 'en'}
```

## 0x07. 集合 set

集合是无序、不重复的元素集合。

```python
# 创建集合
fruits = {'apple', 'banana', 'cherry'}
numbers = {1, 2, 3, 4, 5}
empty_set = set()  # 注意：{} 创建空字典，不是空集合

# 添加/删除元素
fruits.add('date')
fruits.remove('apple')  # 元素不存在时会报错
fruits.discard('fig')   # 元素不存在时不会报错

# 集合运算
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)            # 并集：{1, 2, 3, 4, 5, 6}
print(A & B)            # 交集：{3, 4}
print(A - B)            # 差集：{1, 2}
print(A ^ B)            # 对称差集：{1, 2, 5, 6}

# 集合推导式
squares = {x**2 for x in range(10)}
print(squares)          # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# 去重
nums = [1, 2, 2, 3, 3, 3]
unique = list(set(nums))
print(unique)           # [1, 2, 3]
```

## 0x08. 不可变集合 frozenset

`frozenset` 是不可变的集合，可以用作字典的键。

```python
# 创建 frozenset
fs = frozenset([1, 2, 3])

# 不可变，以下操作会报错
# fs.add(4)  # AttributeError

# 可以用作字典键
cache = {frozenset([1, 2]): 'result1'}
```

## 0x09. None 类型

`None` 表示空值或无值。

```python
# None 是单例
result = None
print(result is None)   # True
print(result == None)   # True (但推荐使用 is)

# 常见用途
def greet(name=None):
    if name is None:
        name = 'World'
    return f'Hello, {name}!'

print(greet())          # Hello, World!
print(greet('Alice'))   # Hello, Alice!
```

## 0x0A. 类型检查和转换

```python
# 类型检查
print(type(42))         # <class 'int'>
print(isinstance(42, int))  # True

# 类型转换
print(int('42'))        # 42
print(float('3.14'))    # 3.14
print(str(42))          # '42'
print(list('abc'))      # ['a', 'b', 'c']
print(tuple([1, 2]))    # (1, 2)
print(set([1, 2, 2]))   # {1, 2}

# 类型注解（Python 3.5+）
def add(a: int, b: int) -> int:
    return a + b
```

## 参考
1. [Python 官方文档 - 数据类型](https://docs.python.org/3/library/datatypes.html)
2. [Python 官方文档 - 内置类型](https://docs.python.org/3/library/stdtypes.html)