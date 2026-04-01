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

## 0x0B. 异步函数（async/await）

异步函数使用 `async def` 定义，通过 `await` 关键字等待异步操作完成。异步函数允许程序在等待 I/O 操作时执行其他任务，提高程序的并发性能。

### 基本概念

```python
"""
协程（Coroutine）：使用 async def 定义的函数，调用后返回协程对象
await：暂停当前协程的执行，等待另一个协程完成
asyncio：Python 的异步 I/O 框架，提供事件循环和协程调度
"""

import asyncio

# 异步函数的定义
async def hello():
    """异步函数使用 async def 定义"""
    print('Hello')
    await asyncio.sleep(1)  # 等待 1 秒（不阻塞事件循环）
    print('World')

# 调用异步函数返回协程对象，不是直接执行
coro = hello()
print(type(coro))  # <class 'coroutine'>

# 使用 asyncio.run() 运行协程
asyncio.run(hello())
# 输出:
# Hello
# (等待1秒)
# World
```

### await 关键字

```python
import asyncio

async def fetch_data():
    """模拟获取数据的异步操作"""
    print('开始获取数据...')
    await asyncio.sleep(2)  # 模拟网络请求
    print('数据获取完成')
    return {'id': 1, 'name': 'Alice'}

async def process_data():
    """等待并处理数据"""
    data = await fetch_data()  # 等待 fetch_data 完成
    print(f'处理数据: {data}')
    return data

# 运行
asyncio.run(process_data())
# 输出:
# 开始获取数据...
# (等待2秒)
# 数据获取完成
# 处理数据: {'id': 1, 'name': 'Alice'}
```

### 并发执行多个协程

```python
import asyncio

async def task(name, delay):
    """模拟异步任务"""
    print(f'任务 {name} 开始')
    await asyncio.sleep(delay)
    print(f'任务 {name} 完成')
    return f'{name} 的结果'

async def main():
    # 方式 1：顺序执行（慢）
    print('=== 顺序执行 ===')
    r1 = await task('A', 2)
    r2 = await task('B', 1)
    print(f'结果: {r1}, {r2}')
    
    # 方式 2：并发执行（快）
    print('\n=== 并发执行 ===')
    results = await asyncio.gather(
        task('C', 2),
        task('D', 1),
        task('E', 3)
    )
    print(f'结果: {results}')

asyncio.run(main())
# 并发执行时，任务同时进行，总耗时约 3 秒（而非 6 秒）
```

### asyncio.gather vs asyncio.create_task

```python
import asyncio

async def fetch_url(url, delay):
    """模拟网络请求"""
    print(f'请求 {url} 开始')
    await asyncio.sleep(delay)
    print(f'请求 {url} 完成')
    return f'{url} 的数据'

async def main():
    # gather：等待所有协程完成
    print('=== 使用 gather ===')
    results = await asyncio.gather(
        fetch_url('api/users', 2),
        fetch_url('api/posts', 1),
        fetch_url('api/comments', 3)
    )
    print(f'结果: {results}\n')
    
    # create_task：创建独立任务，可以分别等待
    print('=== 使用 create_task ===')
    task1 = asyncio.create_task(fetch_url('api/data1', 2))
    task2 = asyncio.create_task(fetch_url('api/data2', 1))
    
    # 可以在任务完成前做其他事情
    print('任务已创建，做其他事情...')
    
    # 等待任务完成
    result1 = await task1
    result2 = await task2
    print(f'结果: {result1}, {result2}')

asyncio.run(main())
```

### 异步上下文管理器

```python
import asyncio

class AsyncDatabaseConnection:
    """异步数据库连接"""
    
    async def __aenter__(self):
        """异步进入上下文"""
        print('正在连接数据库...')
        await asyncio.sleep(1)  # 模拟连接过程
        print('数据库连接成功')
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """异步退出上下文"""
        print('正在关闭数据库连接...')
        await asyncio.sleep(0.5)  # 模拟关闭过程
        print('数据库连接已关闭')
        return False
    
    async def query(self, sql):
        """执行查询"""
        print(f'执行查询: {sql}')
        await asyncio.sleep(0.5)
        return [{'id': 1, 'name': 'Alice'}]

async def main():
    async with AsyncDatabaseConnection() as db:
        results = await db.query('SELECT * FROM users')
        print(f'查询结果: {results}')

asyncio.run(main())
# 输出:
# 正在连接数据库...
# 数据库连接成功
# 执行查询: SELECT * FROM users
# 查询结果: [{'id': 1, 'name': 'Alice'}]
# 正在关闭数据库连接...
# 数据库连接已关闭
```

### 异步迭代器

```python
import asyncio

class AsyncRange:
    """异步范围迭代器"""
    
    def __init__(self, start, stop, delay=0.1):
        self.start = start
        self.stop = stop
        self.delay = delay
        self.current = start
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.current >= self.stop:
            raise StopAsyncIteration
        
        await asyncio.sleep(self.delay)  # 模拟异步操作
        value = self.current
        self.current += 1
        return value

async def main():
    # 异步迭代
    async for i in AsyncRange(0, 5, delay=0.5):
        print(f'获取到值: {i}')
    
    # 异步生成器
    async def async_generator():
        for i in range(5):
            await asyncio.sleep(0.5)
            yield i
    
    print('\n=== 异步生成器 ===')
    async for i in async_generator():
        print(f'生成器产生: {i}')

asyncio.run(main())
```

### 异步队列

```python
import asyncio

async def producer(queue, name, items):
    """生产者：向队列添加数据"""
    for item in items:
        await asyncio.sleep(0.5)  # 模拟生产过程
        await queue.put(f'{name}-{item}')
        print(f'生产者 {name} 生产了: {name}-{item}')
    
    # 发送结束信号
    await queue.put(None)

async def consumer(queue, name):
    """消费者：从队列获取数据"""
    while True:
        item = await queue.get()
        if item is None:
            # 收到结束信号
            await queue.put(None)  # 通知其他消费者
            break
        
        print(f'消费者 {name} 处理了: {item}')
        await asyncio.sleep(0.3)  # 模拟处理过程
        queue.task_done()

async def main():
    # 创建队列
    queue = asyncio.Queue(maxsize=5)
    
    # 启动生产者和消费者
    producer_task = asyncio.create_task(
        producer(queue, 'P1', ['A', 'B', 'C'])
    )
    consumer_task = asyncio.create_task(
        consumer(queue, 'C1')
    )
    
    # 等待生产者完成
    await producer_task
    
    # 等待队列处理完毕
    await queue.join()
    
    # 取消消费者
    consumer_task.cancel()

asyncio.run(main())
```

### 异常处理

```python
import asyncio

async def risky_operation(fail=False):
    """可能失败的异步操作"""
    await asyncio.sleep(1)
    if fail:
        raise ValueError('操作失败')
    return '成功'

async def main():
    # 处理单个协程的异常
    try:
        result = await risky_operation(fail=True)
    except ValueError as e:
        print(f'捕获异常: {e}')
    
    # 使用 gather 处理多个协程的异常
    try:
        results = await asyncio.gather(
            risky_operation(fail=False),
            risky_operation(fail=True),
            risky_operation(fail=False),
            return_exceptions=True  # 返回异常而不是抛出
        )
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                print(f'任务 {i} 失败: {result}')
            else:
                print(f'任务 {i} 成功: {result}')
    except Exception as e:
        print(f'其他异常: {e}')

asyncio.run(main())
```

### 实际应用：并发 HTTP 请求

```python
import asyncio
import aiohttp  # 需要安装: pip install aiohttp

async def fetch_url(session, url):
    """异步获取 URL 内容"""
    try:
        async with session.get(url) as response:
            content = await response.text()
            return {'url': url, 'status': response.status, 'length': len(content)}
    except Exception as e:
        return {'url': url, 'error': str(e)}

async def fetch_all(urls):
    """并发获取多个 URL"""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# 使用示例
async def main():
    urls = [
        'http://example.com',
        'http://example.org',
        'http://example.net',
    ]
    
    results = await fetch_all(urls)
    for result in results:
        print(result)

# 取消注释以运行（需要安装 aiohttp）
# asyncio.run(main())
```

### 最佳实践

```python
"""
1. 使用 asyncio.run() 作为程序入口
2. 避免在异步函数中使用阻塞操作（如 time.sleep）
3. 使用 asyncio.gather() 或 create_task() 实现并发
4. 正确处理异步上下文和异常
5. 使用异步库（aiohttp, aiofiles, asyncpg 等）
"""

import asyncio

# ✅ 正确做法
async def correct_example():
    await asyncio.sleep(1)  # 使用 asyncio.sleep
    return 'done'

# ❌ 错误做法
# async def wrong_example():
#     import time
#     time.sleep(1)  # 阻塞事件循环！
#     return 'done'

# ✅ 异步文件操作
import aiofiles  # 需要安装: pip install aiofiles

async def read_file_async(path):
    async with aiofiles.open(path, 'r') as f:
        content = await f.read()
        return content

# ❌ 阻塞文件操作
# async def read_file_blocking(path):
#     with open(path, 'r') as f:  # 阻塞！
#         return f.read()
```

## 参考
1. [Python 官方文档 - 定义函数](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
2. [Python 官方文档 - 函数注解](https://docs.python.org/3/tutorial/controlflow.html#function-annotations)
3. [PEP 3107 - 函数注解](https://peps.python.org/pep-3107/)
4. [PEP 484 - 类型提示](https://peps.python.org/pep-0484/)
5. [Python 官方文档 - asyncio](https://docs.python.org/3/library/asyncio.html)
6. [PEP 492 - async/await 语法](https://peps.python.org/pep-0492/)