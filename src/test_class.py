"""类的核心知识点测试 - 基于 docs/class.md"""

import math
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List


# ============================================================
# 0x01. 基本类定义
# ============================================================

class TestBasicClass:
    """基本类定义测试"""

    def test_class_definition(self):
        """class关键字定义类"""
        class Animal:
            species_count = 0

            def __init__(self, name, age):
                self.name = name
                self.age = age
                Animal.species_count += 1

            def eat(self):
                return f'{self.name}正在吃东西'

        dog = Animal('旺财', 3)
        cat = Animal('咪咪', 2)

        assert dog.name == '旺财'
        assert dog.age == 3
        assert dog.eat() == '旺财正在吃东西'
        assert Animal.species_count == 2
        assert dog.species_count == 2


# ============================================================
# 0x02. 类变量与实例变量
# ============================================================

class TestClassVsInstanceVar:
    """类变量与实例变量测试"""

    def test_class_variable_shared(self):
        """类变量所有实例共享"""
        class Student:
            school = 'Python University'
            student_count = 0

            def __init__(self, name, grade):
                self.name = name
                self.grade = grade
                Student.student_count += 1

        s1 = Student('Alice', 1)
        s2 = Student('Bob', 2)

        assert Student.school == 'Python University'
        assert s1.school == 'Python University'
        assert Student.student_count == 2
        assert s1.name == 'Alice'
        assert s2.name == 'Bob'

    def test_instance_variable_override(self):
        """修改实例变量不影响类变量"""
        class Student:
            school = 'Python University'

        s1 = Student()
        s1.school = 'New School'
        assert s1.school == 'New School'
        assert Student.school == 'Python University'

    def test_class_variable_change_affects_all(self):
        """修改类变量影响所有实例"""
        class Student:
            school = 'Python University'

        s1 = Student()
        s2 = Student()
        Student.school = 'Updated University'
        assert Student.school == 'Updated University'
        assert s2.school == 'Updated University'


# ============================================================
# 0x03. 方法类型
# ============================================================

class TestMethodTypes:
    """方法类型测试"""

    def test_instance_method(self):
        """实例方法第一个参数是self"""
        class MyClass:
            def instance_method(self):
                return 'instance'

        obj = MyClass()
        assert obj.instance_method() == 'instance'
        assert MyClass.instance_method(obj) == 'instance'

    def test_class_method(self):
        """类方法第一个参数是cls"""
        class MyClass:
            count = 0

            def __init__(self):
                MyClass.count += 1

            @classmethod
            def get_count(cls):
                return cls.count

            @classmethod
            def create_instance(cls):
                return cls()

        assert MyClass.get_count() == 0
        obj1 = MyClass()
        obj2 = MyClass()
        assert MyClass.get_count() == 2

        obj3 = MyClass.create_instance()
        assert MyClass.get_count() == 3

    def test_static_method(self):
        """静态方法不需要访问实例或类"""
        class MathUtils:
            @staticmethod
            def add(a, b):
                return a + b

            @staticmethod
            def is_even(n):
                return n % 2 == 0

        assert MathUtils.add(3, 4) == 7
        assert MathUtils.is_even(4) is True
        assert MathUtils.is_even(3) is False

        obj = MathUtils()
        assert obj.add(3, 4) == 7


# ============================================================
# 0x04. 继承
# ============================================================

class TestInheritance:
    """继承测试"""

    def test_basic_inheritance(self):
        """基本继承"""
        class Animal:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def speak(self):
                return '动物发出声音'

            def info(self):
                return f'{self.name}, {self.age}岁'

        class Dog(Animal):
            def __init__(self, name, age, breed):
                super().__init__(name, age)
                self.breed = breed

            def speak(self):
                return f'{self.name}说: 汪汪!'

            def fetch(self):
                return f'{self.name}正在捡球'

        class Cat(Animal):
            def speak(self):
                return f'{self.name}说: 喵喵!'

        dog = Dog('旺财', 3, '金毛')
        cat = Cat('咪咪', 2)

        assert dog.info() == '旺财, 3岁'
        assert cat.info() == '咪咪, 2岁'
        assert dog.speak() == '旺财说: 汪汪!'
        assert cat.speak() == '咪咪说: 喵喵!'
        assert dog.fetch() == '旺财正在捡球'
        assert dog.breed == '金毛'

    def test_isinstance_issubclass(self):
        """检查继承关系"""
        class Animal:
            pass

        class Dog(Animal):
            pass

        dog = Dog()
        assert isinstance(dog, Dog) is True
        assert isinstance(dog, Animal) is True
        assert issubclass(Dog, Animal) is True

    def test_multiple_inheritance(self):
        """多重继承"""
        class Animal:
            def __init__(self, name, age):
                self.name = name
                self.age = age

        class Flyable:
            def fly(self):
                return '可以飞'

        class Swimmable:
            def swim(self):
                return '可以游泳'

        class Duck(Animal, Flyable, Swimmable):
            def speak(self):
                return f'{self.name}说: 嘎嘎!'

        duck = Duck('唐老鸭', 1)
        assert duck.speak() == '唐老鸭说: 嘎嘎!'
        assert duck.fly() == '可以飞'
        assert duck.swim() == '可以游泳'

    def test_mro(self):
        """方法解析顺序 (MRO)"""
        class A:
            pass

        class B(A):
            pass

        class C(A):
            pass

        class D(B, C):
            pass

        assert D.__mro__[0] is D
        assert D.__mro__[1] is B
        assert D.__mro__[2] is C
        assert D.__mro__[3] is A


# ============================================================
# 0x05. 封装
# ============================================================

class TestEncapsulation:
    """封装测试"""

    def test_public_attribute(self):
        """公有属性"""
        class Person:
            def __init__(self, name, age, ssn):
                self.name = name

        p = Person('Alice', 25, '123-45-6789')
        assert p.name == 'Alice'

    def test_protected_attribute(self):
        """保护属性（约定）"""
        class Person:
            def __init__(self, name, age, ssn):
                self._age = age

        p = Person('Alice', 25, '123-45-6789')
        assert p._age == 25

    def test_private_attribute(self):
        """私有属性（名称改写）"""
        class Person:
            def __init__(self, name, age, ssn):
                self.__ssn = ssn

            def get_ssn(self):
                return self.__ssn

        p = Person('Alice', 25, '123-45-6789')
        assert p.get_ssn() == '123-45-6789'
        assert p._Person__ssn == '123-45-6789'

    def test_private_attribute_access_error(self):
        """直接访问私有属性报AttributeError"""
        class Person:
            def __init__(self, name, age, ssn):
                self.__ssn = ssn

        p = Person('Alice', 25, '123-45-6789')
        try:
            _ = p.__ssn
            assert False, "Should have raised AttributeError"
        except AttributeError:
            pass


# ============================================================
# property 装饰器
# ============================================================

class TestProperty:
    """property装饰器测试"""

    def test_property_getter(self):
        """@property getter"""
        class Circle:
            def __init__(self, radius):
                self._radius = radius

            @property
            def radius(self):
                return self._radius

        c = Circle(5)
        assert c.radius == 5

    def test_property_setter(self):
        """@xxx.setter setter含验证"""
        class Circle:
            def __init__(self, radius):
                self._radius = radius

            @property
            def radius(self):
                return self._radius

            @radius.setter
            def radius(self, value):
                if value < 0:
                    raise ValueError('半径不能为负数')
                self._radius = value

        c = Circle(5)
        c.radius = 10
        assert c.radius == 10

    def test_property_setter_validation(self):
        """setter验证抛出ValueError"""
        class Circle:
            def __init__(self, radius):
                self._radius = radius

            @property
            def radius(self):
                return self._radius

            @radius.setter
            def radius(self, value):
                if value < 0:
                    raise ValueError('半径不能为负数')
                self._radius = value

        c = Circle(5)
        try:
            c.radius = -1
            assert False, "Should have raised ValueError"
        except ValueError as e:
            assert '负数' in str(e)

    def test_read_only_property(self):
        """只读property（无setter）"""
        class Circle:
            def __init__(self, radius):
                self._radius = radius

            @property
            def area(self):
                return math.pi * self._radius ** 2

        c = Circle(5)
        assert abs(c.area - 78.5398) < 0.01

        try:
            c.area = 100
            assert False, "Should have raised AttributeError"
        except AttributeError:
            pass


# ============================================================
# 0x06. 魔术方法
# ============================================================

class TestMagicMethods:
    """魔术方法测试"""

    def test_repr_str(self):
        """__repr__ 和 __str__"""
        class Vector:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def __repr__(self):
                return f'Vector({self.x}, {self.y})'

            def __str__(self):
                return f'({self.x}, {self.y})'

        v = Vector(3, 4)
        assert repr(v) == 'Vector(3, 4)'
        assert str(v) == '(3, 4)'

    def test_arithmetic_operators(self):
        """算术运算符重载"""
        class Vector:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def __add__(self, other):
                return Vector(self.x + other.x, self.y + other.y)

            def __sub__(self, other):
                return Vector(self.x - other.x, self.y - other.y)

            def __mul__(self, scalar):
                return Vector(self.x * scalar, self.y * scalar)

        v1 = Vector(3, 4)
        v2 = Vector(1, 2)

        v3 = v1 + v2
        assert v3.x == 4 and v3.y == 6

        v4 = v1 - v2
        assert v4.x == 2 and v4.y == 2

        v5 = v1 * 2
        assert v5.x == 6 and v5.y == 8

    def test_eq_operator(self):
        """相等运算符重载"""
        class Vector:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def __eq__(self, other):
                return self.x == other.x and self.y == other.y

        v1 = Vector(3, 4)
        v2 = Vector(3, 4)
        v3 = Vector(1, 2)
        assert v1 == v2
        assert v1 != v3

    def test_abs_len(self):
        """abs()和len()函数"""
        class Vector:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def __abs__(self):
                return (self.x ** 2 + self.y ** 2) ** 0.5

            def __len__(self):
                return int(abs(self))

        v = Vector(3, 4)
        assert abs(v) == 5.0
        assert len(v) == 5

    def test_getitem_iter(self):
        """索引访问和迭代"""
        class Vector:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def __getitem__(self, index):
                if index == 0:
                    return self.x
                elif index == 1:
                    return self.y
                raise IndexError('向量索引超出范围')

            def __iter__(self):
                yield self.x
                yield self.y

        v = Vector(3, 4)
        assert v[0] == 3
        assert v[1] == 4

        try:
            _ = v[2]
            assert False, "Should have raised IndexError"
        except IndexError:
            pass

        assert list(v) == [3, 4]


# ============================================================
# 0x07. 抽象类
# ============================================================

class TestAbstractClass:
    """抽象类测试"""

    def test_cannot_instantiate_abstract_class(self):
        """不能实例化抽象类"""
        class Shape(ABC):
            @abstractmethod
            def area(self):
                pass

            @abstractmethod
            def perimeter(self):
                pass

        try:
            Shape()
            assert False, "Should have raised TypeError"
        except TypeError:
            pass

    def test_concrete_class_must_implement(self):
        """子类必须实现抽象方法"""
        class Shape(ABC):
            @abstractmethod
            def area(self):
                pass

            @abstractmethod
            def perimeter(self):
                pass

        class Rectangle(Shape):
            def __init__(self, width, height):
                self.width = width
                self.height = height

            def area(self):
                return self.width * self.height

            def perimeter(self):
                return 2 * (self.width + self.height)

        rect = Rectangle(5, 3)
        assert rect.area() == 15
        assert rect.perimeter() == 16

    def test_abstract_class_concrete_method(self):
        """具体方法可以继承"""
        class Shape(ABC):
            @abstractmethod
            def area(self):
                pass

            @abstractmethod
            def perimeter(self):
                pass

            def description(self):
                return f'面积: {self.area():.2f}, 周长: {self.perimeter():.2f}'

        class Rectangle(Shape):
            def __init__(self, width, height):
                self.width = width
                self.height = height

            def area(self):
                return self.width * self.height

            def perimeter(self):
                return 2 * (self.width + self.height)

        rect = Rectangle(5, 3)
        assert '面积' in rect.description()
        assert '周长' in rect.description()


# ============================================================
# 0x08. 数据类 (Python 3.7+)
# ============================================================

class TestDataClass:
    """数据类测试"""

    def test_dataclass_auto_methods(self):
        """自动生成__init__, __repr__, __eq__"""
        @dataclass
        class Student:
            name: str
            age: int
            grades: List[float] = field(default_factory=list)

            def average_grade(self) -> float:
                return sum(self.grades) / len(self.grades) if self.grades else 0.0

        s1 = Student('Alice', 20, [85, 90, 78])
        s2 = Student('Bob', 21, [92, 88, 95])
        assert 'Alice' in repr(s1)
        assert s1 != s2
        assert abs(s1.average_grade() - 84.33) < 0.1

    def test_dataclass_default_factory(self):
        """field(default_factory=list)"""
        @dataclass
        class Student:
            name: str
            age: int
            grades: List[float] = field(default_factory=list)

        s1 = Student('Alice', 20)
        s2 = Student('Bob', 21)
        s1.grades.append(90)
        assert s1.grades == [90]
        assert s2.grades == []

    def test_frozen_dataclass(self):
        """frozen=True不可变"""
        @dataclass(frozen=True)
        class Point:
            x: float
            y: float

        p = Point(3.0, 4.0)
        assert p.x == 3.0
        assert p.y == 4.0

        try:
            p.x = 5.0
            assert False, "Should have raised FrozenInstanceError"
        except AttributeError:
            pass


# ============================================================
# 0x09. 枚举类
# ============================================================

class TestEnum:
    """枚举类测试"""

    def test_enum_basic(self):
        """枚举基本使用"""
        class Color(Enum):
            RED = 1
            GREEN = 2
            BLUE = 3

        assert Color.RED.value == 1
        assert Color.RED.name == 'RED'

    def test_enum_auto(self):
        """auto()自动赋值"""
        class Status(Enum):
            PENDING = auto()
            RUNNING = auto()
            COMPLETED = auto()
            FAILED = auto()

        assert Status.PENDING.value == 1
        assert Status.RUNNING.value == 2
        assert Status.COMPLETED.value == 3
        assert Status.FAILED.value == 4

    def test_enum_from_value(self):
        """从值获取枚举"""
        class Status(Enum):
            PENDING = auto()
            RUNNING = auto()
            COMPLETED = auto()

        status = Status(2)
        assert status == Status.RUNNING

    def test_enum_comparison(self):
        """枚举比较"""
        class Color(Enum):
            RED = 1
            GREEN = 2
            BLUE = 3

        assert Color.RED == Color.RED
        assert Color.RED != Color.BLUE

    def test_enum_iteration(self):
        """遍历枚举"""
        class Color(Enum):
            RED = 1
            GREEN = 2
            BLUE = 3

        names = [c.name for c in Color]
        assert names == ['RED', 'GREEN', 'BLUE']
