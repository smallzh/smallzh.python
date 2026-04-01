# Python 运行模型

Python 的运行模型定义了代码如何被组织、执行和管理变量。理解这些概念对于写出高效、正确的 Python 代码至关重要。

## 0x01. 代码块（Code Block）

代码块是 Python 程序中作为一个单元执行的文本段。

### 代码块的类型

```python
"""
Python 中的代码块包括：
- 模块（Module）：整个 .py 文件
- 函数体（Function Body）：函数定义内的代码
- 类定义（Class Definition）：类定义内的代码
- 交互式命令：Python REPL 中的每条命令
- 脚本文件：通过 python 命令执行的文件
- eval() 和 exec() 的参数
"""

# 1. 模块代码块
# 文件 module.py 的所有内容构成一个代码块
x = 10
y = 20

# 2. 函数代码块
def my_function():
    # 这是一个函数代码块
    local_var = 100
    return local_var

# 3. 类代码块
class MyClass:
    # 这是一个类代码块
    class_var = 42
    
    def method(self):
        # 这是一个方法代码块（也是函数代码块）
        return self.class_var

# 4. 交互式命令
# >>> x = 1  # 每行命令都是一个代码块

# 5. exec() 执行的代码
code = """
result = 1 + 2
print(result)
"""
exec(code)
```

### 代码块的执行

```python
# 代码块在执行帧（Execution Frame）中执行

# 每个代码块都有自己的命名空间
x = 'global'  # 模块级命名空间

def func():
    x = 'local'  # 函数级命名空间
    print(x)

func()      # 输出: local
print(x)    # 输出: global

# 类代码块有特殊的行为
class MyClass:
    x = 'class'
    
    def method(self):
        # 方法不能直接访问类代码块的局部变量
        # 需要通过 self 或类名访问
        return self.x  # 或 MyClass.x

obj = MyClass()
print(obj.method())  # 输出: class
```

## 0x02. 命名与绑定（Naming and Binding）

命名是给对象起名字，绑定是将名字与对象关联起来。

### 绑定操作

```python
"""
以下操作会创建绑定：
- 赋值语句（=）
- for 循环变量
- 函数定义
- 类定义
- import 语句
- as 子句
- 异常捕获（except ... as ...）
"""

# 1. 赋值绑定
x = 42  # x 绑定到整数对象 42

# 2. for 循环绑定
for i in [1, 2, 3]:  # i 绑定到列表中的每个元素
    print(i)

# 3. 函数定义绑定
def my_func():  # my_func 绑定到函数对象
    pass

# 4. 类定义绑定
class MyClass:  # MyClass 绑定到类对象
    pass

# 5. import 绑定
import os  # os 绑定到 os 模块对象
from sys import path  # path 绑定到 sys.path

# 6. as 子句绑定
with open('file.txt') as f:  # f 绑定到文件对象
    pass

# 7. 异常绑定
try:
    raise ValueError('error')
except ValueError as e:  # e 绑定到异常对象
    print(e)
```

### 绑定的作用域

```python
# 全局绑定
global_var = 'global'

def func():
    # 局部绑定
    local_var = 'local'
    
    # 使用 global 声明修改全局绑定
    global global_var
    global_var = 'modified'

def outer():
    # 闭包中的绑定
    x = 'outer'
    
    def inner():
        # 使用 nonlocal 声明修改外层绑定
        nonlocal x
        x = 'modified'
    
    inner()
    return x

print(outer())  # 'modified'
```

### del 语句

```python
# del 解除绑定（不是删除对象）
x = [1, 2, 3]
y = x  # y 和 x 绑定到同一个对象

del x  # 解除 x 的绑定
# print(x)  # NameError: name 'x' is not defined

print(y)  # [1, 2, 3] - 对象仍然存在

# del 也可以删除容器中的元素
lst = [1, 2, 3, 4, 5]
del lst[0]
print(lst)  # [2, 3, 4, 5]

del lst[1:3]
print(lst)  # [2, 5]

# 删除字典中的键
d = {'a': 1, 'b': 2}
del d['a']
print(d)  # {'b': 2}
```

## 0x03. 作用域（Scope）

作用域定义了名称在代码块中的可见性范围。

### 作用域类型

```python
"""
Python 有四种作用域（LEGB 规则）：
- Local（局部）：函数内部
- Enclosing（闭包）：外层函数（嵌套函数时）
- Global（全局）：模块级别
- Built-in（内置）：Python 内置名称
"""

# 示例：LEGB 规则
x = 'global x'  # Global 作用域

def outer():
    x = 'outer x'  # Enclosing 作用域
    
    def inner():
        x = 'inner x'  # Local 作用域
        print(x)  # 输出: inner x
    
    inner()
    print(x)  # 输出: outer x

outer()
print(x)  # 输出: global x
```

### 变量查找顺序

```python
# Python 按 L -> E -> G -> B 的顺序查找变量

# 示例 1：Local 覆盖
x = 'global'
def func():
    x = 'local'  # Local
    print(x)  # 'local'
func()

# 示例 2：使用 Enclosing
def outer():
    x = 'enclosing'
    def inner():
        print(x)  # 找到 Enclosing 中的 x
    inner()
outer()

# 示例 3：使用 Global
x = 'global'
def func():
    print(x)  # 找到 Global 中的 x
func()

# 示例 4：使用 Built-in
# len 是内置函数
print(len([1, 2, 3]))  # 找到 Built-in 中的 len

# 如果定义了同名的局部变量
def func():
    len = 100  # Local
    # len([1, 2, 3])  # TypeError: 'int' object is not callable
    print(len)  # 100
func()
```

### global 和 nonlocal 声明

```python
# global 声明：使用全局变量
x = 10

def modify_global():
    global x
    x = 20  # 修改全局变量 x

modify_global()
print(x)  # 20

# nonlocal 声明：使用外层函数变量
def outer():
    x = 10
    
    def inner():
        nonlocal x
        x = 20  # 修改外层函数的 x
    
    inner()
    print(x)  # 20

outer()

# 注意：nonlocal 不能用于全局变量
x = 10
def func():
    # nonlocal x  # SyntaxError: no binding for nonlocal 'x' found
    pass
```

## 0x04. 命名空间（Namespace）

命名空间是从名称到对象的映射，实现名称的绑定和查找。

### 命名空间的类型

```python
"""
命名空间的类型：
- 内置命名空间：包含内置函数和异常（启动时创建）
- 全局命名空间：模块级别的名称（模块加载时创建）
- 局部命名空间：函数内的名称（函数调用时创建）
"""

# 查看命名空间
import sys

# 内置命名空间
print('len' in dir(__builtins__))  # True

# 全局命名空间
x = 10
print('x' in globals())  # True

def func():
    y = 20
    # 局部命名空间
    print('y' in locals())  # True

func()
```

### 命名空间的生命周期

```python
# 1. 内置命名空间：Python 解释器启动时创建，关闭时销毁

# 2. 全局命名空间：模块加载时创建，解释器关闭时销毁
#    通常存储在模块的 __dict__ 中

import sys
print(sys.modules[__name__] is sys.modules['__main__'])  # True

# 3. 局部命名空间：函数调用时创建，函数返回时销毁

def func():
    x = 10
    print(locals())  # {'x': 10}
    return x

func()
# 函数返回后，局部命名空间被销毁

# 4. 嵌套函数的命名空间
def outer():
    x = 10
    def inner():
        y = 20
        print(locals())  # {'y': 20}
    inner()
    print(locals())  # {'x': 10, 'inner': <function>}

outer()
```

### 命名空间与作用域的关系

```python
"""
作用域是静态概念（代码文本中的区域）
命名空间是动态概念（运行时的映射结构）

作用域决定"去哪里找"
命名空间决定"能找到什么"
"""

x = 'global'

def func():
    # 作用域：这个函数的代码区域
    # 命名空间：{'x': 'local'} 这个字典
    
    x = 'local'
    
    def inner():
        # inner 的作用域可以访问 func 的命名空间
        # 通过闭包机制实现
        print(x)
    
    inner()
```

## 0x05. 执行帧（Execution Frame）

执行帧是代码执行时的上下文环境，包含代码、命名空间和执行状态。

### 帧对象

```python
import sys
import inspect

def func():
    # 获取当前帧
    frame = sys._getframe()
    
    print(f'当前函数: {frame.f_code.co_name}')
    print(f'局部变量: {frame.f_locals}')
    print(f'全局变量: {frame.f_globals}')
    
    # 调用栈
    print(f'调用者: {frame.f_back.f_code.co_name}')

def caller():
    func()

caller()

# 使用 inspect 模块
def show_stack():
    stack = inspect.stack()
    for frame_info in stack:
        print(f'{frame_info.function} in {frame_info.filename}:{frame_info.lineno}')

def wrapper():
    show_stack()

wrapper()
```

### 递归与栈帧

```python
import sys

def factorial(n):
    # 查看当前栈深度
    frame = sys._getframe()
    depth = 0
    f = frame
    while f.f_back:
        depth += 1
        f = f.f_back
    
    print(f'factorial({n}) - 栈深度: {depth}')
    
    if n <= 1:
        return 1
    return n * factorial(n - 1)

result = factorial(5)
print(f'结果: {result}')

# 递归深度限制
print(f'默认递归限制: {sys.getrecursionlimit()}')

# 修改递归限制（谨慎使用）
# sys.setrecursionlimit(10000)
```

## 0x06. 闭包与自由变量

闭包是一个函数对象，它记住了创建时的环境。

### 闭包的形成

```python
def make_counter():
    count = 0  # 自由变量
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

# 创建闭包
counter1 = make_counter()
counter2 = make_counter()

print(counter1())  # 1
print(counter1())  # 2
print(counter2())  # 1 - 独立的计数器

# 检查闭包
print(counter1.__closure__)  # (<cell object at ...>,)
print(counter1.__code__.co_freevars)  # ('count',)
```

### 闭包与延迟绑定

```python
# 经典陷阱：循环中的闭包
funcs = []
for i in range(3):
    def func():
        return i
    funcs.append(func)

print(funcs[0]())  # 2
print(funcs[1]())  # 2
print(funcs[2]())  # 2
# 所有函数都引用同一个 i，最终值是 2

# 解决方案 1：使用默认参数
funcs = []
for i in range(3):
    def func(i=i):  # 默认参数在定义时绑定
        return i
    funcs.append(func)

print(funcs[0]())  # 0
print(funcs[1]())  # 1
print(funcs[2]())  # 2

# 解决方案 2：使用闭包工厂
funcs = []
for i in range(3):
    def make_func(x):
        def func():
            return x
        return func
    funcs.append(make_func(i))

print(funcs[0]())  # 0
print(funcs[1]())  # 1
print(funcs[2]())  # 2

# 解决方案 3：使用 functools.partial
from functools import partial

funcs = []
for i in range(3):
    funcs.append(partial(lambda x: x, i))

print(funcs[0]())  # 0
print(funcs[1]())  # 1
print(funcs[2]())  # 2
```

## 0x07. globals() 和 locals()

```python
# globals() 返回全局命名空间的字典
# locals() 返回局部命名空间的字典

x = 10
y = 20

# 在全局作用域中
print(type(globals()))  # <class 'dict'>
print('x' in globals())  # True
print(globals()['x'])  # 10

# 在函数中
def func(a, b):
    c = a + b
    print('局部命名空间:', locals())  # {'a': 1, 'b': 2, 'c': 3}
    print('全局命名空间中的 x:', globals()['x'])  # 10

func(1, 2)

# 动态执行代码
code = """
result = x + y
"""
exec(code, globals())
print(result)  # 30

# 修改局部命名空间（有限制）
def func():
    x = 10
    locals()['x'] = 20  # 这样修改不会生效
    print(x)  # 10

func()

# 但可以修改全局命名空间
globals()['new_var'] = 100
print(new_var)  # 100
```

## 0x08. 延迟求值（Lazy Evaluation）

延迟求值是指表达式的求值被推迟到实际需要结果时。

### 生成器

```python
# 生成器是延迟求值的典型例子
def generate_numbers():
    print('开始生成')
    for i in range(3):
        print(f'生成: {i}')
        yield i
    print('生成结束')

# 创建生成器时不会执行代码
gen = generate_numbers()

# 只有在需要时才执行
print('第一次 next:')
print(next(gen))  # 开始生成 \n 生成: 0 \n 0

print('第二次 next:')
print(next(gen))  # 生成: 1 \n 1

# 生成器表达式
gen = (x * x for x in range(5))
print(type(gen))  # <class 'generator'>
print(next(gen))  # 0
print(next(gen))  # 1
```

### 类型注解的延迟求值

```python
from typing import List, Optional

# Python 3.7+ 支持延迟求值的类型注解
# 使用 from __future__ import annotations
from __future__ import annotations

class Node:
    # 类型注解中的前向引用
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next
    
    def to_list(self) -> List[int]:
        result = []
        current: Optional[Node] = self
        while current:
            result.append(current.value)
            current = current.next
        return result

# 创建链表
node = Node(1, Node(2, Node(3)))
print(node.to_list())  # [1, 2, 3]
```

### 惰性迭代器

```python
import itertools

# itertools 中的惰性迭代器
# count() - 无限计数
counter = itertools.count(1)
print(next(counter))  # 1
print(next(counter))  # 2

# cycle() - 无限循环
colors = itertools.cycle(['red', 'green', 'blue'])
print(next(colors))  # 'red'
print(next(colors))  # 'green'

# islice() - 惰性切片
numbers = (x * x for x in range(1000000))
squares = itertools.islice(numbers, 5)
print(list(squares))  # [0, 1, 4, 9, 16]
```

## 0x09. 异常处理机制

### 异常的传播

```python
# 异常沿着调用栈向上传播
def level3():
    raise ValueError('错误发生在 level3')

def level2():
    level3()

def level1():
    try:
        level2()
    except ValueError as e:
        print(f'捕获到异常: {e}')
        # 查看调用栈
        import traceback
        traceback.print_exc()

level1()
```

### 异常上下文

```python
# 异常链
try:
    try:
        raise ValueError('原始错误')
    except ValueError as e:
        raise RuntimeError('包装错误') from e
except RuntimeError as e:
    print(f'错误: {e}')
    print(f'原因: {e.__cause__}')

# 隐藏异常上下文
try:
    raise ValueError('原始错误')
except ValueError:
    raise RuntimeError('新错误') from None
```

### finally 与资源清理

```python
# finally 块总是执行
def risky_operation():
    try:
        print('执行操作')
        return '结果'
    finally:
        print('清理资源')  # 即使有 return 也会执行

result = risky_operation()
# 输出:
# 执行操作
# 清理资源
print(result)  # 结果

# 上下文管理器自动处理
class Resource:
    def __enter__(self):
        print('获取资源')
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('释放资源')
        return False  # 不抑制异常

with Resource():
    print('使用资源')
# 输出:
# 获取资源
# 使用资源
# 释放资源
```

## 参考
1. [Python 官方文档 - 执行模型](https://docs.python.org/3/reference/executionmodel.html)
2. [Python 官方文档 - 数据模型](https://docs.python.org/3/reference/datamodel.html)
3. [PEP 563 - 延迟求值的注解](https://peps.python.org/pep-0563/)