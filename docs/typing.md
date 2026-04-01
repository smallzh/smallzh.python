# 类型提示

Python 3.5+ 支持类型提示（Type Hints），用于提高代码可读性和 IDE 支持。

## 0x01. 基本类型提示

```python
# 基本类型注解
def greet(name: str) -> str:
    return f'Hello, {name}!'

def add(a: int, b: int) -> int:
    return a + b

# 变量注解
name: str = 'Alice'
age: int = 25
pi: float = 3.14
is_active: bool = True

# 没有返回值
def print_message(message: str) -> None:
    print(message)
```

## 0x02. 复杂类型

### typing 模块

```python
from typing import List, Dict, Tuple, Set, Optional, Union, Any, Callable

# 列表
numbers: List[int] = [1, 2, 3]
names: List[str] = ['Alice', 'Bob']

# 字典
scores: Dict[str, int] = {'Alice': 90, 'Bob': 85}
config: Dict[str, Any] = {'debug': True, 'port': 8080}

# 元组
point: Tuple[float, float] = (10.0, 20.0)
record: Tuple[int, str, bool] = (1, 'Alice', True)

# 集合
unique_ids: Set[int] = {1, 2, 3}

# 可选类型（可能是 None）
def find_user(user_id: int) -> Optional[str]:
    users = {1: 'Alice', 2: 'Bob'}
    return users.get(user_id)

# 等价写法
def find_user(user_id: int) -> str | None:  # Python 3.10+
    users = {1: 'Alice', 2: 'Bob'}
    return users.get(user_id)

# 联合类型
def process(value: Union[int, str]) -> str:
    return str(value)

# 等价写法（Python 3.10+）
def process(value: int | str) -> str:
    return str(value)

# 可调用对象
def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

# 使用
def add(a: int, b: int) -> int:
    return a + b

result = apply(add, 3, 4)  # 7
```

### Python 3.9+ 泛型语法

```python
# Python 3.9+ 可以直接使用内置类型
numbers: list[int] = [1, 2, 3]
scores: dict[str, int] = {'Alice': 90}
point: tuple[float, float] = (10.0, 20.0)
unique: set[int] = {1, 2, 3}

# Python 3.10+ 联合类型
def process(value: int | str) -> str:
    return str(value)

# Python 3.10+ 可选类型
def find_user(user_id: int) -> str | None:
    return None
```

## 0x03. 泛型

```python
from typing import TypeVar, Generic

# TypeVar - 类型变量
T = TypeVar('T')

def first_element(lst: list[T]) -> T:
    return lst[0]

# 使用
num = first_element([1, 2, 3])      # 推断为 int
text = first_element(['a', 'b'])    # 推断为 str

# 约束类型变量
T = TypeVar('T', int, float, str)

def add(a: T, b: T) -> T:
    return a + b

# 泛型类
from typing import Generic, TypeVar

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        return self._items.pop()
    
    def peek(self) -> T:
        return self._items[-1]

# 使用
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)

str_stack: Stack[str] = Stack()
str_stack.push('a')
str_stack.push('b')
```

## 0x04. 高级类型

### TypedDict

```python
from typing import TypedDict

# 定义字典结构
class UserDict(TypedDict):
    name: str
    age: int
    email: str

# 使用
user: UserDict = {
    'name': 'Alice',
    'age': 25,
    'email': 'alice@example.com'
}

# 可选字段
class UserDictOptional(TypedDict, total=False):
    name: str
    age: int
    email: str  # 所有字段都可选

# 混合必需和可选字段
class UserDictMixed(TypedDict):
    name: str  # 必需
    age: int   # 必需

class UserDictComplete(UserDictMixed, total=False):
    email: str  # 可选
    phone: str  # 可选
```

### Literal

```python
from typing import Literal

# 字面量类型
def set_direction(direction: Literal['up', 'down', 'left', 'right']) -> None:
    print(f'Direction: {direction}')

set_direction('up')      # OK
set_direction('forward') # 类型检查器会报错

# 数字字面量
def set_port(port: Literal[80, 443, 8080]) -> None:
    print(f'Port: {port}')

# 组合字面量
LogLevel = Literal['debug', 'info', 'warning', 'error']
```

### Final

```python
from typing import Final

# 常量
MAX_SIZE: Final[int] = 100
PI: Final[float] = 3.14159

# 不能重新赋值（类型检查器会警告）
# MAX_SIZE = 200  # Error

# Final 类（不能被继承）
from typing import Final

class Immutable:
    pass

class Child(Immutable):  # 类型检查器会警告
    pass
```

## 0x05. 类别类型

### Type

```python
from typing import Type

class Animal:
    def speak(self) -> str:
        return '...'

class Dog(Animal):
    def speak(self) -> str:
        return 'Woof!'

# 接受类本身（不是实例）
def create_animal(animal_type: Type[Animal]) -> Animal:
    return animal_type()

# 使用
dog = create_animal(Dog)
print(dog.speak())  # Woof!
```

### ClassVar

```python
from typing import ClassVar

class MyClass:
    # 类变量
    count: ClassVar[int] = 0
    
    def __init__(self) -> None:
        MyClass.count += 1

# 类型检查器会确保 count 是类变量
obj1 = MyClass()
obj2 = MyClass()
print(MyClass.count)  # 2
```

## 0x06. 类型别名

```python
from typing import List, Dict, Tuple, Union

# 类型别名
Vector = List[float]
Matrix = List[Vector]
UserId = int
UserName = str
UserMap = Dict[UserId, UserName]

# 使用
def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# Python 3.10+ 新语法
type Vector = list[float]
type Matrix = list[Vector]

# 复杂类型别名
Coordinate = Tuple[float, float]
BoundingBox = Tuple[Coordinate, Coordinate]
JSON = Union[str, int, float, bool, None, Dict[str, 'JSON'], List['JSON']]
```

## 0x07. 协议（Protocol）

```python
from typing import Protocol

# 定义协议（结构化子类型）
class Drawable(Protocol):
    def draw(self) -> None: ...

# 实现协议的类
class Circle:
    def draw(self) -> None:
        print('Drawing circle')

class Square:
    def draw(self) -> None:
        print('Drawing square')

# 使用协议类型
def render(shape: Drawable) -> None:
    shape.draw()

# Circle 和 Square 都符合 Drawable 协议
render(Circle())  # OK
render(Square())  # OK
```

## 0x08. 类型检查工具

### mypy

```shell
# 安装
pip install mypy

# 运行检查
mypy script.py
mypy src/

# 配置 mypy.ini
[mypy]
python_version = 3.11
warn_return_any = True
warn_unused_configs = True
```

### pyright

```shell
# VS Code 扩展
# 安装 Pylance 扩展

# 配置 pyrightconfig.json
{
    "pythonVersion": "3.11",
    "typeCheckingMode": "basic"
}
```

## 0x09. 实际应用

### API 类型安全

```python
from typing import TypedDict, Optional
from dataclasses import dataclass

# API 响应类型
class ApiResponse(TypedDict):
    status: int
    message: str
    data: Optional[dict]

# 数据模型
@dataclass
class User:
    id: int
    name: str
    email: str
    age: Optional[int] = None

def get_user(user_id: int) -> ApiResponse:
    user = User(id=user_id, name='Alice', email='alice@example.com')
    return {
        'status': 200,
        'message': 'Success',
        'data': {'user': user.__dict__}
    }
```

### 配置类型

```python
from typing import TypedDict, Literal
from pathlib import Path

class DatabaseConfig(TypedDict):
    host: str
    port: int
    username: str
    password: str

class AppConfig(TypedDict):
    debug: bool
    log_level: Literal['DEBUG', 'INFO', 'WARNING', 'ERROR']
    database: DatabaseConfig
    static_dir: Path

config: AppConfig = {
    'debug': True,
    'log_level': 'DEBUG',
    'database': {
        'host': 'localhost',
        'port': 5432,
        'username': 'admin',
        'password': 'secret'
    },
    'static_dir': Path('/var/www/static')
}
```

### 验证器

```python
from typing import TypeVar, Callable, Any
from functools import wraps

T = TypeVar('T')

def validate(**validators: Callable[[Any], bool]) -> Callable:
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            # 验证逻辑
            for name, validator in validators.items():
                if name in kwargs and not validator(kwargs[name]):
                    raise ValueError(f'Invalid value for {name}')
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 使用
@validate(age=lambda x: 0 <= x <= 150)
def create_user(name: str, age: int) -> dict:
    return {'name': name, 'age': age}

# create_user('Alice', age=25)  # OK
# create_user('Bob', age=200)   # ValueError
```

## 参考
1. [PEP 484 - Type Hints](https://peps.python.org/pep-0484/)
2. [PEP 526 - Syntax for Variable Annotations](https://peps.python.org/pep-0526/)
3. [Python typing 模块文档](https://docs.python.org/3/library/typing.html)
4. [mypy 文档](https://mypy.readthedocs.io/)