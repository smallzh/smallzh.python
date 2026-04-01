# 定义函数

函数是组织好的、可重复使用的、用来实现单一或相关联功能的代码段。

## 0x01. 基本函数定义

```python
# 使用 def 关键字定义函数
def greet():
    """这是一个简单的问候函数"""
    print('Hello, World!')

# 调用函数
greet()  # Hello, World!

# 带参数的函数
def greet(name):
    """问候指定的人"""
    print(f'Hello, {name}!')

greet('Alice')  # Hello, Alice!

# 带返回值的函数
def add(a, b):
    """返回两个数的和"""
    return a + b

result = add(3, 5)
print(result)  # 8

# 返回多个值
def get_coordinates():
    """返回坐标点"""
    return 10, 20

x, y = get_coordinates()
print(f'x: {x}, y: {y}')  # x: 10, y: 20
```

## 0x02. 函数参数

### 位置参数

```python
def power(base, exponent):
    """计算 base 的 exponent 次方"""
    return base ** exponent

print(power(2, 3))  # 8
print(power(3, 2))  # 9
```

### 默认参数

```python
def greet(name, greeting='Hello'):
    """带默认问候语的函数"""
    print(f'{greeting}, {name}!')

greet('Alice')           # Hello, Alice!
greet('Bob', 'Hi')       # Hi, Bob!

# 默认参数必须在非默认参数之后
# def greet(greeting='Hello', name):  # SyntaxError
#     pass

# 默认参数陷阱：避免使用可变对象作为默认参数
def append_to_list(item, lst=[]):  # 错误示例
    lst.append(item)
    return lst

print(append_to_list(1))  # [1]
print(append_to_list(2))  # [1, 2] - 不是 [2]！

# 正确做法
def append_to_list(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(append_to_list(1))  # [1]
print(append_to_list(2))  # [2]
```

### 关键字参数

```python
def describe_pet(animal_type, pet_name):
    """描述宠物"""
    print(f"I have a {animal_type} named {pet_name}.")

# 使用关键字参数
describe_pet(animal_type='hamster', pet_name='Harry')
describe_pet(pet_name='Tom', animal_type='cat')  # 可以改变顺序
describe_pet('dog', 'Rex')  # 位置参数
describe_pet(animal_type='bird', 'Polly')  # SyntaxError: 位置参数必须在关键字参数之前
```

### *args 可变位置参数

```python
def sum_all(*args):
    """计算所有参数的和"""
    print(f'args 类型: {type(args)}')  # <class 'tuple'>
    print(f'args 内容: {args}')
    return sum(args)

print(sum_all(1, 2, 3))        # args 类型: <class 'tuple'>  args 内容: (1, 2, 3)  6
print(sum_all(1, 2, 3, 4, 5))  # 15

# 混合使用
def func(required, *args):
    print(f'required: {required}')
    print(f'args: {args}')

func(1, 2, 3, 4)  # required: 1  args: (2, 3, 4)
```

### **kwargs 可变关键字参数

```python
def print_info(**kwargs):
    """打印所有关键字参数"""
    print(f'kwargs 类型: {type(kwargs)}')  # <class 'dict'>
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_info(name='Alice', age=25, city='Beijing')
# kwargs 类型: <class 'dict'>
# name: Alice
# age: 25
# city: Beijing

# 混合使用
def func(a, b, *args, **kwargs):
    print(f'a: {a}, b: {b}')
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')

func(1, 2, 3, 4, x=5, y=6)
# a: 1, b: 2
# args: (3, 4)
# kwargs: {'x': 5, 'y': 6}
```

### 仅关键字参数

```python
# 使用 * 分隔符，后面的参数必须使用关键字传递
def func(a, b, *, c, d):
    print(a, b, c, d)

func(1, 2, c=3, d=4)  # OK
# func(1, 2, 3, 4)    # TypeError: func() takes 2 positional arguments but 4 were given
```

### 仅位置参数（Python 3.8+）

```python
# 使用 / 分隔符，前面的参数只能使用位置传递
def func(a, b, /, c, d):
    print(a, b, c, d)

func(1, 2, 3, 4)      # OK
func(1, 2, c=3, d=4)  # OK
# func(a=1, b=2, c=3, d=4)  # TypeError: func() got some positional-only arguments passed as keyword arguments
```

## 0x03. 解包参数

```python
def add(a, b, c):
    return a + b + c

# 解包列表或元组
args = [1, 2, 3]
print(add(*args))  # 6

# 解包字典
kwargs = {'a': 1, 'b': 2, 'c': 3}
print(add(**kwargs))  # 6

# 混合解包
args = [1, 2]
kwargs = {'c': 3}
print(add(*args, **kwargs))  # 6
```

## 0x04. 匿名函数 lambda

```python
# 基本语法：lambda 参数: 表达式
square = lambda x: x ** 2
print(square(5))  # 25

# 多个参数
add = lambda a, b: a + b
print(add(3, 4))  # 7

# 带默认参数
greet = lambda name, greeting='Hello': f'{greeting}, {name}!'
print(greet('Alice'))  # Hello, Alice!

# 在高阶函数中使用
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# 排序时使用
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)  # [(1, 'one'), (3, 'three'), (2, 'two')]
```

## 0x05. 闭包

闭包是指一个函数记住了它的定义作用域，即使该函数在其定义作用域之外被调用。

```python
def make_multiplier(factor):
    """返回一个乘以 factor 的函数"""
    def multiplier(x):
        return x * factor
    return multiplier

# 创建闭包
double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15

# 闭包可以访问外部函数的变量
def counter():
    count = 0
    def increment():
        nonlocal count  # 声明使用外部变量
        count += 1
        return count
    return increment

c = counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
```

## 0x06. 装饰器

装饰器是修改其他函数功能的函数。

```python
# 基本装饰器
def my_decorator(func):
    def wrapper():
        print('在函数执行前')
        func()
        print('在函数执行后')
    return wrapper

@my_decorator
def say_hello():
    print('Hello!')

say_hello()
# 在函数执行前
# Hello!
# 在函数执行后

# 带参数的装饰器
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f'Hello, {name}!')

greet('Alice')
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!

# 保留原函数信息的装饰器
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """包装函数的文档"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def say_hello():
    """原始函数的文档"""
    print('Hello!')

print(say_hello.__name__)    # say_hello (不是 wrapper)
print(say_hello.__doc__)     # 原始函数的文档
```

## 0x07. 生成器函数

使用 `yield` 关键字的函数是生成器函数。

```python
def count_up_to(n):
    """生成从 1 到 n 的数字"""
    i = 1
    while i <= n:
        yield i
        i += 1

# 使用生成器
for num in count_up_to(5):
    print(num)
# 1 2 3 4 5

# 生成器表达式
squares = (x ** 2 for x in range(5))
print(list(squares))  # [0, 1, 4, 9, 16]

# 生成器惰性求值
def fibonacci():
    """斐波那契数列生成器"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 取前 10 个斐波那契数
fib = fibonacci()
fib_numbers = [next(fib) for _ in range(10)]
print(fib_numbers)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## 0x08. 递归函数

```python
# 阶乘
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120

# 斐波那契数列（递归，效率较低）
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # 55

# 使用缓存优化递归
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

print(fibonacci_cached(100))  # 354224848179261915075
```

## 0x09. 类型注解

Python 3.5+ 支持类型注解，用于提高代码可读性和IDE支持。

```python
# 基本类型注解
def add(a: int, b: int) -> int:
    return a + b

# 复杂类型注解
from typing import List, Dict, Tuple, Optional, Union

def process_items(items: List[str]) -> Dict[str, int]:
    """处理项目列表，返回统计字典"""
    return {item: len(item) for item in items}

def get_coordinates() -> Tuple[float, float]:
    return (10.0, 20.0)

def find_user(user_id: int) -> Optional[str]:
    """返回用户名或 None"""
    users = {1: 'Alice', 2: 'Bob'}
    return users.get(user_id)

# Union 类型
def process(value: Union[int, str]) -> str:
    return str(value)

# Python 3.10+ 使用 | 语法
def process_new(value: int | str) -> str:
    return str(value)

# 可调用对象类型
from typing import Callable

def apply_func(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

result = apply_func(add, 3, 4)
```

## 0x0A. 文档字符串

```python
def complex_function(param1: int, param2: str = 'default') -> bool:
    """
    这是一个复杂函数的简短描述。

    这里是更详细的描述，可以包含多行。
    解释函数的工作原理、使用场景等。

    Args:
        param1: 第一个参数的描述
        param2: 第二个参数的描述，默认值为 'default'

    Returns:
        布尔值，表示操作是否成功

    Raises:
        ValueError: 当 param1 为负数时抛出

    Examples:
        >>> complex_function(42, 'hello')
        True
        >>> complex_function(-1)
        ValueError: param1 must be non-negative
    """
    if param1 < 0:
        raise ValueError('param1 must be non-negative')
    return True

# 使用 help() 查看文档
help(complex_function)

# 使用 __doc__ 属性
print(complex_function.__doc__)
```

## 参考
1. [Python 官方文档 - 定义函数](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
2. [Python 官方文档 - 函数注解](https://docs.python.org/3/tutorial/controlflow.html#function-annotations)
3. [PEP 3107 - 函数注解](https://peps.python.org/pep-3107/)
4. [PEP 484 - 类型提示](https://peps.python.org/pep-0484/)