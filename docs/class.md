# 使用类

类，从编程语言角度来说，就是把`数据`和`函数`打包在一起

使用关键字`class` 来定义类，如：
```python
class Animal:
    """类注释"""
    name = '旺财'
    
    def __init__(self, age):
        self.age = age
        pass
    
    def eat(self):
        return '开饭啦'
    
# 类的使用方式
## 直接以 className.name 方式使用
### 属于类变量，用于所有实例共享
print(Animal.name)
print(Animal.age)
print(Animal.__doc__)
## 这种 className.fun 方式，是以 函数对象 的方式来使用，因此，eat叫 函数
print(Animal.eat())
## 创建类实例 来使用
animal = Animal(1)
print(animal.name)
### 属于实例变量，用于单独实例 使用
print(animal.age)
## 这种 classInstance.fun 方式， 是以 方法对象 的方式来使用，因此，eat叫 方法
## 和 className.fun的差别，相当于 classInstance.fun = className.fun(classInstance)
print(animal.eat())
```

class本身也是一个对象，即，类对象。

>  When a non-data attribute of an instance is referenced, the instance’s class is searched. If the name denotes a valid class attribute that is a function object, a method object is created by packing (pointers to) the instance object and the function object just found together in an abstract object: this is the method object. When the method object is called with an argument list, a new argument list is constructed from the instance object and the argument list, and the function object is called with this new argument list.
> 
> 当一个实例的非数据属性被引用时，将搜索实例所属的类。 如果被引用的属性名称表示一个有效的类属性中的函数对象，会通过打包（指向）查找到的实例对象和函数对象到一个抽象对象的方式来创建方法对象：这个抽象对象就是方法对象。 当附带参数列表调用方法对象时，将基于实例对象和参数列表构建一个新的参数列表，并使用这个新参数列表调用相应的函数对象。

最终，类中 变量的定义位置，取决于它的使用范围，如果仅是 类实例中使用，就定义在 __init__中，如果是所有类实例共享，就定义在 类里面。

可以使用`object.__class__` 来获取实例对象的类型。

```python
print(Animal.__class__)
```

## 继承
语法格式为
```python
# 也可以使用 class className(moduleName.BaseClassName) 方式
class Dog(Animal):
    """演示 继承"""

    def __init__(self):
        pass

    def bark(self):
        return 'bark...'

## 使用
dog = Dog()
print(dog.eat())
print(dog.bark())
```
可以使用以下两个方法来检测是否继承：
1. isinstance，检测对象是否为某个类的实例
2. issubclass，检测类是否为另一个类的之类

支持supper()方法的使用，但多继承中，如何明确具体的supper？

多重继承的格式如下：
```python
class className(Base1, Base2, Base3):
    """多重继承"""

    def __init(self):
        pass
```

这里面有一个疑问？父类的__init__方法参数如何传？

## 私有变量
class中并不存在私有变量，但，有规定

在变量、方法的命名前面加上 `_`或`__` 后，被视为私有的

```python
class cat:
    """私有变量"""

    def __init__(self):
        self.__sex = 1

    def __set(self):
        pass
```

这种假私有的变量、方法，可以通过`_[className]__[name]`形式来访问

## 数据类
可以使用`dataclasses模块里的dataclass装饰器`，声明一个类为数据类

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int

student = Student('xiaoming', 10)
print(student.name)
```

## 1 类

## 2 静态方法
使用注解 @staticmethod 

问题：
为什么会用静态方法

## 3 类方法

使用注解 @classmethod 

暂时理解成，升级版的 静态方法？