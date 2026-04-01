# 使用类

类，从编程语言角度来说，就是把`数据`和`函数`打包在一起。

## 0x01. 基本类定义

使用关键字`class` 来定义类：

```python
class Animal:
    """动物类的示例"""
    
    # 类变量：所有实例共享
    species_count = 0
    
    def __init__(self, name, age):
        """构造方法"""
        self.name = name  # 实例变量
        self.age = age
        Animal.species_count += 1
    
    def eat(self):
        """实例方法"""
        return f'{self.name} 正在吃东西'
    
    def speak(self):
        """子类需要重写的方法"""
        raise NotImplementedError('子类必须实现 speak 方法')

# 创建实例
dog = Animal('旺财', 3)
cat = Animal('咪咪', 2)

# 访问实例变量
print(dog.name)  # 旺财
print(dog.age)   # 3

# 调用实例方法
print(dog.eat())  # 旺财正在吃东西

# 访问类变量
print(Animal.species_count)  # 2
print(dog.species_count)     # 2 (通过实例访问类变量)
```

## 0x02. 类变量与实例变量

```python
class Student:
    # 类变量：所有实例共享
    school = 'Python University'
    student_count = 0
    
    def __init__(self, name, grade):
        # 实例变量：每个实例独有
        self.name = name
        self.grade = grade
        Student.student_count += 1
    
    def display(self):
        print(f'{self.name} - {self.grade}年级 - {Student.school}')

# 创建实例
s1 = Student('Alice', 1)
s2 = Student('Bob', 2)

# 类变量
print(Student.school)  # Python University
print(s1.school)       # Python University (通过实例访问)
print(Student.student_count)  # 2

# 实例变量
print(s1.name)  # Alice
print(s2.name)  # Bob

# 修改实例变量不会影响类变量
s1.school = 'New School'
print(s1.school)       # New School
print(Student.school)  # Python University
print(s2.school)       # Python University

# 修改类变量会影响所有实例
Student.school = 'Updated University'
print(Student.school)  # Updated University
print(s1.school)       # New School (实例变量已覆盖)
print(s2.school)       # Updated University
```

## 0x03. 方法类型

### 实例方法

```python
class MyClass:
    def instance_method(self):
        """实例方法：第一个参数是 self，代表实例本身"""
        return f'调用实例方法，实例: {self}'

obj = MyClass()
print(obj.instance_method())  # 通过实例调用
print(MyClass.instance_method(obj))  # 通过类调用（等价）
```

### 类方法

```python
class MyClass:
    count = 0
    
    def __init__(self):
        MyClass.count += 1
    
    @classmethod
    def get_count(cls):
        """类方法：第一个参数是 cls，代表类本身"""
        return f'当前实例数量: {cls.count}'
    
    @classmethod
    def create_instance(cls):
        """工厂方法：使用类方法创建实例"""
        return cls()

# 使用类方法
print(MyClass.get_count())  # 当前实例数量: 0

obj1 = MyClass()
obj2 = MyClass()
print(MyClass.get_count())  # 当前实例数量: 2

# 使用工厂方法
obj3 = MyClass.create_instance()
print(MyClass.get_count())  # 当前实例数量: 3
```

### 静态方法

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        """静态方法：不需要访问实例或类"""
        return a + b
    
    @staticmethod
    def is_even(n):
        return n % 2 == 0

# 使用静态方法（不需要创建实例）
print(MathUtils.add(3, 4))    # 7
print(MathUtils.is_even(4))   # True

# 也可以通过实例调用
obj = MathUtils()
print(obj.add(3, 4))  # 7
```

## 0x04. 继承

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        return '动物发出声音'
    
    def info(self):
        return f'{self.name}, {self.age}岁'

class Dog(Animal):
    """继承自 Animal 类"""
    
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # 调用父类构造方法
        self.breed = breed
    
    def speak(self):
        """重写父类方法"""
        return f'{self.name}说: 汪汪!'
    
    def fetch(self):
        """子类特有方法"""
        return f'{self.name}正在捡球'

class Cat(Animal):
    def speak(self):
        return f'{self.name}说: 喵喵!'

# 创建实例
dog = Dog('旺财', 3, '金毛')
cat = Cat('咪咪', 2)

# 继承的方法
print(dog.info())    # 旺财, 3岁
print(cat.info())    # 咪咪, 2岁

# 重写的方法
print(dog.speak())   # 旺财说: 汪汪!
print(cat.speak())   # 咪咪说: 喵喵!

# 子类特有方法
print(dog.fetch())   # 旺财正在捡球

# 检查继承关系
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True
print(issubclass(Dog, Animal))  # True
```

### 多重继承

```python
class Flyable:
    def fly(self):
        return '可以飞'

class Swimmable:
    def swim(self):
        return '可以游泳'

class Duck(Animal, Flyable, Swimmable):
    """鸭子：会飞、会游泳"""
    
    def speak(self):
        return f'{self.name}说: 嘎嘎!'
    
    def info(self):
        return f'{super().info()}, 会飞、会游泳'

duck = Duck('唐老鸭', 1)
print(duck.speak())  # 唐老鸭说: 嘎嘎!
print(duck.fly())    # 可以飞
print(duck.swim())   # 可以游泳

# 查看方法解析顺序 (MRO)
print(Duck.__mro__)
# (<class '__main__.Duck'>, <class '__main__.Animal'>, <class '__main__.Flyable'>, <class '__main__.Swimmable'>, <class 'object'>)
```

## 0x05. 封装

### 公有、保护、私有属性

```python
class Person:
    def __init__(self, name, age, ssn):
        self.name = name          # 公有属性
        self._age = age           # 保护属性（约定）
        self.__ssn = ssn          # 私有属性（名称改写）
    
    def get_ssn(self):
        """通过方法访问私有属性"""
        return self.__ssn
    
    def _internal_method(self):
        """保护方法（约定）"""
        return '内部方法'
    
    def __private_method(self):
        """私有方法"""
        return '私有方法'

p = Person('Alice', 25, '123-45-6789')

# 公有属性
print(p.name)  # Alice

# 保护属性（可以访问，但不建议）
print(p._age)  # 25

# 私有属性（通过名称改写访问）
print(p._Person__ssn)  # 123-45-6789
# print(p.__ssn)  # AttributeError

# 通过公有方法访问
print(p.get_ssn())  # 123-45-6789
```

### property 装饰器

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """获取半径"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """设置半径，带验证"""
        if value < 0:
            raise ValueError('半径不能为负数')
        self._radius = value
    
    @property
    def area(self):
        """计算面积（只读属性）"""
        import math
        return math.pi * self._radius ** 2

# 使用 property
c = Circle(5)
print(c.radius)  # 5
print(c.area)    # 78.53981633974483

c.radius = 10
print(c.radius)  # 10
print(c.area)    # 314.1592653589793

# c.area = 100  # AttributeError: can't set attribute
# c.radius = -1  # ValueError: 半径不能为负数
```

## 0x06. 魔术方法

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        """官方字符串表示"""
        return f'Vector({self.x}, {self.y})'
    
    def __str__(self):
        """用户友好的字符串表示"""
        return f'({self.x}, {self.y})'
    
    def __add__(self, other):
        """加法运算符重载"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """减法运算符重载"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """乘法运算符重载"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        """相等运算符重载"""
        return self.x == other.x and self.y == other.y
    
    def __abs__(self):
        """abs() 函数"""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __len__(self):
        """len() 函数"""
        return int(abs(self))
    
    def __getitem__(self, index):
        """索引访问"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError('向量索引超出范围')
    
    def __iter__(self):
        """迭代器"""
        yield self.x
        yield self.y

# 使用
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(repr(v1))       # Vector(3, 4)
print(str(v1))        # (3, 4)
print(v1 + v2)        # (4, 6)
print(v1 - v2)        # (2, 2)
print(v1 * 2)         # (6, 8)
print(v1 == v2)       # False
print(abs(v1))        # 5.0
print(len(v1))        # 5
print(v1[0])          # 3
print(v1[1])          # 4

# 迭代
for coord in v1:
    print(coord)
# 3
# 4
```

## 0x07. 抽象类

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """抽象基类"""
    
    @abstractmethod
    def area(self):
        """抽象方法：子类必须实现"""
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def description(self):
        """具体方法：子类可以继承"""
        return f'面积: {self.area():.2f}, 周长: {self.perimeter():.2f}'

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# 不能实例化抽象类
# shape = Shape()  # TypeError

# 实例化具体类
rect = Rectangle(5, 3)
print(rect.description())  # 面积: 15.00, 周长: 16.00

circle = Circle(5)
print(circle.description())  # 面积: 78.54, 周长: 31.42
```

## 0x08. 数据类（Python 3.7+）

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Student:
    name: str
    age: int
    grades: List[float] = field(default_factory=list)
    
    def average_grade(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

# 自动生成 __init__, __repr__, __eq__ 等方法
s1 = Student('Alice', 20, [85, 90, 78])
s2 = Student('Bob', 21, [92, 88, 95])

print(s1)           # Student(name='Alice', age=20, grades=[85, 90, 78])
print(s1 == s2)     # False
print(s1.average_grade())  # 84.33333333333333

# 不可变数据类
@dataclass(frozen=True)
class Point:
    x: float
    y: float

p = Point(3.0, 4.0)
# p.x = 5.0  # FrozenInstanceError
```

## 0x09. 枚举类

```python
from enum import Enum, auto

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Status(Enum):
    PENDING = auto()
    RUNNING = auto()
    COMPLETED = auto()
    FAILED = auto()

# 使用枚举
print(Color.RED)        # Color.RED
print(Color.RED.value)  # 1
print(Color.RED.name)   # RED

# 遍历枚举
for color in Color:
    print(f'{color.name}: {color.value}')

# 从值获取枚举
status = Status(2)
print(status)  # Status.RUNNING

# 比较
print(Color.RED == Color.RED)   # True
print(Color.RED == Color.BLUE)  # False
```

## 参考
1. [Python 官方文档 - 类](https://docs.python.org/3/tutorial/classes.html)
2. [Python 官方文档 - 数据模型](https://docs.python.org/3/reference/datamodel.html)
3. [PEP 557 - 数据类](https://peps.python.org/pep-0557/)