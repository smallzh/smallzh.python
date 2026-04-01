# 流程控制

每种编程语言都会有自己的**流程控制**方式，也就是程序的执行流程，无非下面这几种：
1. 顺序执行
2. 执行分支
3. 循环执行

顺序执行，比较好理解，就是一行行的执行代码。

## 0x01. 条件语句

执行分支，Python提供了以下几种方式：
1. if...elif....elif....else
2. match语句（Python 3.10+）

### if...elif...else

```python
# 基本 if 语句
age = 18
if age >= 18:
    print('你是成年人')

# if-else
age = 15
if age >= 18:
    print('你是成年人')
else:
    print('你是未成年人')

# if-elif-else
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f'你的成绩等级是: {grade}')  # B

# 嵌套 if
age = 25
has_license = True
if age >= 18:
    if has_license:
        print('你可以开车')
    else:
        print('你需要先考驾照')
else:
    print('你还不能开车')

# 条件表达式（三元运算符）
age = 20
status = '成年' if age >= 18 else '未成年'
print(status)  # 成年

# 多条件判断
x = 15
if x > 0 and x < 10:
    print('x 在 0 到 10 之间')
elif x >= 10 and x < 20:
    print('x 在 10 到 20 之间')

# 使用 in 判断
fruit = 'apple'
if fruit in ['apple', 'banana', 'orange']:
    print(f'{fruit} 是常见水果')

# 真值测试
# 以下值在布尔上下文中为 False：False, None, 0, 0.0, '', [], {}, set()
items = []
if items:
    print('列表不为空')
else:
    print('列表为空')

# 链式比较
x = 15
if 10 < x < 20:
    print('x 在 10 到 20 之间')
```

### match 语句（Python 3.10+）

`match` 语句类似于其他语言的 `switch` 语句，但功能更强大。

```python
# 基本 match 语句
status = 404
match status:
    case 200:
        print('OK')
    case 404:
        print('Not Found')
    case 500:
        print('Internal Server Error')
    case _:
        print('Unknown status')

# 匹配多个值
day = 'Monday'
match day:
    case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday':
        print('工作日')
    case 'Saturday' | 'Sunday':
        print('周末')

# 使用 if 守卫
point = (1, 2)
match point:
    case (0, 0):
        print('原点')
    case (x, 0):
        print(f'x 轴上的点: {x}')
    case (0, y):
        print(f'y 轴上的点: {y}')
    case (x, y) if x == y:
        print(f'对角线上的点: ({x}, {y})')
    case (x, y):
        print(f'普通点: ({x}, {y})')

# 匹配类实例
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def locate(point):
    match point:
        case Point(x=0, y=0):
            print('原点')
        case Point(x=x, y=0):
            print(f'x 轴: {x}')
        case Point(x=0, y=y):
            print(f'y 轴: {y}')
        case Point(x=x, y=y):
            print(f'点: ({x}, {y})')

locate(Point(0, 0))   # 原点
locate(Point(5, 0))   # x 轴: 5
locate(Point(0, 3))   # y 轴: 3
locate(Point(2, 3))   # 点: (2, 3)

# 匹配字典
user = {'name': 'Alice', 'age': 25}
match user:
    case {'name': str(name), 'age': int(age)} if age >= 18:
        print(f'{name} 是成年人')
    case {'name': str(name), 'age': int(age)}:
        print(f'{name} 是未成年人')
    case _:
        print('无效用户数据')
```

## 0x02. 循环语句

Python 提供了两种循环语句：
1. while 循环
2. for 循环

### while 循环

```python
# 基本 while 循环
count = 0
while count < 5:
    print(count)
    count += 1
# 输出: 0 1 2 3 4

# 使用 break 跳出循环
n = 0
while True:
    if n >= 5:
        break
    print(n)
    n += 1
# 输出: 0 1 2 3 4

# 使用 continue 跳过本次循环
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)
# 输出: 1 3 5 7 9

# while-else：循环正常结束时执行 else
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print('循环正常结束')
# 输出: 0 1 2 3 4 循环正常结束

# 如果循环被 break 中断，else 不会执行
count = 0
while count < 5:
    if count == 3:
        break
    print(count)
    count += 1
else:
    print('这行不会执行')
# 输出: 0 1 2
```

### for 循环

```python
# 遍历列表
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
# 输出: apple banana cherry

# 遍历字典
person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
for key in person:
    print(f'{key}: {person[key]}')

# 使用 items() 方法
for key, value in person.items():
    print(f'{key}: {value}')

# 遍历字符串
for char in 'Hello':
    print(char)
# 输出: H e l l o

# 使用 range() 函数
for i in range(5):
    print(i)
# 输出: 0 1 2 3 4

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)
# 输出: 0 2 4 6 8

# 反向遍历
for i in range(5, 0, -1):
    print(i)
# 输出: 5 4 3 2 1

# 使用 enumerate() 获取索引
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f'{index}: {fruit}')
# 输出: 0: apple 1: banana 2: cherry

# 指定起始索引
for index, fruit in enumerate(fruits, start=1):
    print(f'{index}: {fruit}')
# 输出: 1: apple 2: banana 3: cherry

# 并行遍历多个序列
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f'{name} is {age} years old')

# for-else
for i in range(5):
    if i == 10:  # 不会发生
        break
    print(i)
else:
    print('循环正常结束')
# 输出: 0 1 2 3 4 循环正常结束
```

## 0x03. 循环控制语句

### break

```python
# break 立即终止循环
for i in range(10):
    if i == 5:
        break
    print(i)
# 输出: 0 1 2 3 4

# 在嵌套循环中，break 只跳出最内层循环
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(f'({i}, {j})')
# 输出: (0, 0) (1, 0) (2, 0)
```

### continue

```python
# continue 跳过本次循环的剩余语句
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# 输出: 1 3 5 7 9
```

### pass

```python
# pass 是空语句，用于占位
for i in range(5):
    pass  # TODO: 实现循环体

# 在定义空函数或类时使用
def function_to_implement():
    pass

class EmptyClass:
    pass
```

## 0x04. 列表推导式

列表推导式提供了一种简洁的创建列表的方式。

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

# 带条件的嵌套推导式
even_flat = [num for row in matrix for num in row if num % 2 == 0]
print(even_flat)  # [2, 4, 6, 8]

# 多变量推导式
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 条件表达式
labels = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
print(labels)  # ['even', 'odd', 'even', 'odd', 'even']
```

### 字典推导式

```python
# 基本语法：{key_expr: value_expr for item in iterable}
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 带条件的推导式
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# 从两个列表创建字典
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
print(d)  # {'a': 1, 'b': 2, 'c': 3}
```

### 集合推导式

```python
# 基本语法：{expression for item in iterable}
squares = {x**2 for x in range(10)}
print(squares)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# 带条件
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0, 4, 16, 36, 64}
```

## 0x05. 常搭配的函数

### range()

```python
# range(stop)
print(list(range(5)))  # [0, 1, 2, 3, 4]

# range(start, stop)
print(list(range(2, 7)))  # [2, 3, 4, 5, 6]

# range(start, stop, step)
print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]
print(list(range(10, 0, -2))) # [10, 8, 6, 4, 2]
```

### len()

```python
# 获取长度
print(len([1, 2, 3]))       # 3
print(len('hello'))         # 5
print(len({'a': 1, 'b': 2})) # 2
```

### enumerate()

```python
# 获取索引和值
fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    print(f'{i}: {fruit}')

# 指定起始索引
for i, fruit in enumerate(fruits, 1):
    print(f'{i}: {fruit}')
```

### zip()

```python
# 并行遍历多个序列
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f'{name}: {age}')

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

### sorted()

```python
# 排序
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted(numbers))  # [1, 1, 2, 3, 4, 5, 6, 9]

# 反向排序
print(sorted(numbers, reverse=True))  # [9, 6, 5, 4, 3, 2, 1, 1]

# 自定义排序
words = ['banana', 'Apple', 'cherry']
print(sorted(words))  # ['Apple', 'banana', 'cherry'] (按 ASCII)
print(sorted(words, key=str.lower))  # ['Apple', 'banana', 'cherry']

# 按字典值排序
students = [
    {'name': 'Alice', 'grade': 88},
    {'name': 'Bob', 'grade': 95},
    {'name': 'Charlie', 'grade': 82}
]
sorted_students = sorted(students, key=lambda x: x['grade'], reverse=True)
print(sorted_students)
```

## 参考
1. [Python 官方文档 - 流程控制](https://docs.python.org/3/tutorial/controlflow.html)
2. [Python 官方文档 - match 语句](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement)