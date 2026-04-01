# 迭代器和生成器

迭代器和生成器是 Python 中处理序列数据的重要工具，提供了惰性求值和内存高效的数据处理方式。

## 0x01. 迭代器协议

迭代器是实现了迭代器协议的对象，该协议包含两个方法：
- `__iter__()`: 返回迭代器对象本身
- `__next__()`: 返回下一个值，如果没有更多元素则抛出 `StopIteration` 异常

```python
# 以类的方式使用迭代器
class Reverse:
    """反向迭代器"""
    
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

# 使用迭代器
rev = Reverse('spam')
for char in rev:
    print(char)
# 输出: m a p s

# 手动调用迭代器方法
rev = Reverse('abc')
it = iter(rev)  # 调用 __iter__
print(next(it))  # 调用 __next__，输出: c
print(next(it))  # 输出: b
print(next(it))  # 输出: a
# print(next(it))  # StopIteration
```

### 可迭代对象 vs 迭代器

```python
# 可迭代对象：实现了 __iter__ 方法的对象
# 迭代器：实现了 __iter__ 和 __next__ 方法的对象

class MyRange:
    """自定义 range 类"""
    
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def __iter__(self):
        """返回一个新的迭代器对象"""
        return MyRangeIterator(self.start, self.stop)

class MyRangeIterator:
    """迭代器类"""
    
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# 使用
my_range = MyRange(0, 5)
print(list(my_range))  # [0, 1, 2, 3, 4]

# 可以多次迭代
for i in my_range:
    print(i)
# 0 1 2 3 4
```

## 0x02. 内置迭代器函数

```python
# iter() - 获取迭代器
s = 'hello'
it = iter(s)
print(next(it))  # h
print(next(it))  # e

# iter() 带两个参数：callable 和 sentinel
# 重复调用 callable 直到返回 sentinel 值
import functools
with open('data.txt', 'r') as f:
    for line in iter(f.readline, ''):
        print(line.strip())

# next() - 获取下一个值
it = iter([1, 2, 3])
print(next(it))      # 1
print(next(it, 'end'))  # 2
print(next(it, 'end'))  # 3
print(next(it, 'end'))  # end (默认值)

# enumerate() - 带索引的迭代
fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    print(f'{i}: {fruit}')

# zip() - 并行迭代
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f'{name}: {age}')

# map() - 对每个元素应用函数
numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x**2, numbers)
print(list(squares))  # [1, 4, 9, 16, 25]

# filter() - 过滤元素
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # [2, 4]

# itertools 模块提供了更多迭代器工具
import itertools

# islice() - 切片迭代器
numbers = itertools.count(1)  # 无限计数器
first_five = list(itertools.islice(numbers, 5))
print(first_five)  # [1, 2, 3, 4, 5]

# chain() - 链接多个迭代器
a = [1, 2, 3]
b = [4, 5, 6]
combined = list(itertools.chain(a, b))
print(combined)  # [1, 2, 3, 4, 5, 6]

# cycle() - 循环迭代器
colors = itertools.cycle(['red', 'green', 'blue'])
for _ in range(5):
    print(next(colors))
# red green blue red green
```

## 0x03. 生成器

生成器是一种特殊的迭代器，使用 `yield` 关键字定义。生成器函数每次调用 `yield` 时暂停执行，并在下次迭代时从暂停处继续。

```python
# 基本生成器函数
def count_up_to(n):
    """生成从 1 到 n 的数字"""
    i = 1
    while i <= n:
        yield i
        i += 1

# 使用生成器
counter = count_up_to(5)
print(next(counter))  # 1
print(next(counter))  # 2

# 在循环中使用
for num in count_up_to(5):
    print(num)
# 1 2 3 4 5

# 生成器的特点：惰性求值，节省内存
import sys
numbers_list = [x for x in range(10000)]
numbers_gen = (x for x in range(10000))

print(sys.getsizeof(numbers_list))  # ~87624 字节
print(sys.getsizeof(numbers_gen))   # ~200 字节
```

### 生成器函数详解

```python
# 斐波那契数列生成器
def fibonacci():
    """生成无限斐波那契数列"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 获取前 10 个斐波那契数
fib = fibonacci()
for _ in range(10):
    print(next(fib))
# 0 1 1 2 3 5 8 13 21 34

# 文件逐行读取生成器
def read_lines(filename):
    """逐行读取文件"""
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

# 使用
# for line in read_lines('data.txt'):
#     print(line)

# 生成器发送值
def accumulator():
    """累加器生成器"""
    total = 0
    while True:
        value = yield total
        if value is not None:
            total += value

acc = accumulator()
next(acc)  # 初始化生成器
print(acc.send(10))  # 10
print(acc.send(20))  # 30
print(acc.send(30))  # 60

# 生成器抛出异常
def generator_with_exception():
    try:
        yield 1
        yield 2
        yield 3
    except ValueError:
        print('捕获到 ValueError')
        yield 'error'

gen = generator_with_exception()
print(next(gen))  # 1
print(gen.throw(ValueError))  # 捕获到 ValueError，输出: error
```

### 生成器方法

```python
# send() - 向生成器发送值
def echo_generator():
    """回显生成器"""
    while True:
        received = yield
        print(f'接收到: {received}')

gen = echo_generator()
next(gen)  # 初始化
gen.send('hello')  # 接收到: hello
gen.send('world')  # 接收到: world

# throw() - 向生成器抛出异常
def safe_generator():
    try:
        yield 1
        yield 2
    except ValueError:
        yield 'caught ValueError'
    except TypeError:
        yield 'caught TypeError'

gen = safe_generator()
print(next(gen))  # 1
print(gen.throw(ValueError))  # caught ValueError

# close() - 关闭生成器
def my_generator():
    try:
        yield 1
        yield 2
    finally:
        print('生成器被关闭')

gen = my_generator()
print(next(gen))  # 1
gen.close()  # 生成器被关闭
```

## 0x04. 生成器表达式

生成器表达式是创建生成器的简洁方式，语法类似列表推导式，但使用圆括号。

```python
# 生成器表达式
squares = (x**2 for x in range(10))
print(type(squares))  # <class 'generator'>

# 惰性求值
print(next(squares))  # 0
print(next(squares))  # 1

# 在函数中直接使用
print(sum(x**2 for x in range(10)))  # 285
print(max(x**2 for x in range(10)))  # 81

# 链式生成器
numbers = range(10)
squares = (x**2 for x in numbers)
even_squares = (x for x in squares if x % 2 == 0)
print(list(even_squares))  # [0, 4, 16, 36, 64]

# 对比列表推导式和生成器表达式
import sys

# 列表推导式：立即创建所有元素
list_comp = [x**2 for x in range(1000)]
print(sys.getsizeof(list_comp))  # ~8856 字节

# 生成器表达式：惰性求值
gen_expr = (x**2 for x in range(1000))
print(sys.getsizeof(gen_expr))  # ~200 字节

# 实际使用时才计算
for i, val in enumerate(gen_expr):
    if i >= 5:
        break
    print(val)
# 0 1 4 9 16
```

## 0x05. 列表推导式

列表推导式是创建列表的简洁方式。

```python
# 基本语法：[expression for item in iterable]
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 带条件的推导式
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# 嵌套推导式
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 条件表达式
labels = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
print(labels)  # ['even', 'odd', 'even', 'odd', 'even']

# 字典推导式
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 集合推导式
squares_set = {x**2 for x in range(10)}
print(squares_set)  # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
```

## 0x06. itertools 模块

`itertools` 模块提供了许多高效的迭代器工具。

```python
import itertools

# count() - 无限计数器
counter = itertools.count(start=1, step=2)
for _ in range(5):
    print(next(counter))
# 1 3 5 7 9

# cycle() - 无限循环
colors = itertools.cycle(['red', 'green', 'blue'])
for _ in range(5):
    print(next(colors))
# red green blue red green

# repeat() - 重复值
ones = itertools.repeat(1, times=5)
print(list(ones))  # [1, 1, 1, 1, 1]

# chain() - 链接多个迭代器
a = [1, 2, 3]
b = ['a', 'b', 'c']
combined = list(itertools.chain(a, b))
print(combined)  # [1, 2, 3, 'a', 'b', 'c']

# islice() - 切片迭代器
data = range(100)
sliced = list(itertools.islice(data, 10, 20, 2))
print(sliced)  # [10, 12, 14, 16, 18]

# filterfalse() - 过滤假值
numbers = range(10)
evens = list(itertools.filterfalse(lambda x: x % 2, numbers))
print(evens)  # [0, 2, 4, 6, 8]

# takewhile() - 取到条件为假
numbers = [1, 2, 3, 4, 5, 1, 2]
taken = list(itertools.takewhile(lambda x: x < 4, numbers))
print(taken)  # [1, 2, 3]

# dropwhile() - 丢弃到条件为假
dropped = list(itertools.dropwhile(lambda x: x < 4, numbers))
print(dropped)  # [4, 5, 1, 2]

# starmap() - 类似 map，但解包参数
pairs = [(2, 3), (4, 5), (6, 7)]
results = list(itertools.starmap(lambda x, y: x * y, pairs))
print(results)  # [6, 20, 42]

# product() - 笛卡尔积
colors = ['red', 'green']
sizes = ['S', 'M', 'L']
products = list(itertools.product(colors, sizes))
print(products)
# [('red', 'S'), ('red', 'M'), ('red', 'L'), ('green', 'S'), ('green', 'M'), ('green', 'L')]

# permutations() - 排列
items = [1, 2, 3]
perms = list(itertools.permutations(items, 2))
print(perms)
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# combinations() - 组合
combs = list(itertools.combinations(items, 2))
print(combs)
# [(1, 2), (1, 3), (2, 3)]

# groupby() - 分组
data = [('A', 1), ('A', 2), ('B', 3), ('B', 4), ('A', 5)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(f'{key}: {list(group)}')
# A: [('A', 1), ('A', 2)]
# B: [('B', 3), ('B', 4)]
# A: [('A', 5)]
```

## 0x07. 生成器最佳实践

```python
# 1. 处理大文件时使用生成器
def read_large_file(filepath):
    """逐行读取大文件，避免内存溢出"""
    with open(filepath, 'r') as f:
        for line in f:
            yield line.strip()

# 2. 管道式处理数据
def read_data(filename):
    """读取数据"""
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

def parse_data(lines):
    """解析数据"""
    for line in lines:
        yield line.split(',')

def filter_data(records):
    """过滤数据"""
    for record in records:
        if len(record) == 3:
            yield record

# 组合使用
# lines = read_data('data.csv')
# records = parse_data(lines)
# valid_records = filter_data(records)
# for record in valid_records:
#     print(record)

# 3. 无限序列生成器
def prime_numbers():
    """生成素数"""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

# 获取前 10 个素数
primes = prime_numbers()
first_10_primes = [next(primes) for _ in range(10)]
print(first_10_primes)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# 4. 生成器状态机
def state_machine():
    """简单的状态机"""
    state = 'INIT'
    while True:
        if state == 'INIT':
            value = yield '等待输入'
            if value == 'start':
                state = 'RUNNING'
        elif state == 'RUNNING':
            value = yield '运行中'
            if value == 'stop':
                state = 'STOPPED'
        elif state == 'STOPPED':
            yield '已停止'
            break

sm = state_machine()
print(next(sm))        # 等待输入
print(sm.send('start'))  # 运行中
print(sm.send('stop'))   # 已停止
```

## 参考
1. [Python 官方文档 - 迭代器](https://docs.python.org/3/tutorial/classes.html#iterators)
2. [Python 官方文档 - 生成器](https://docs.python.org/3/tutorial/classes.html#generators)
3. [Python 官方文档 - itertools 模块](https://docs.python.org/3/library/itertools.html)
4. [PEP 255 - 简单生成器](https://peps.python.org/pep-0255/)