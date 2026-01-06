
## 0x01: object的关键点
在Python中，一切 皆是 objects。

每一个object包含3个成分：一个标识（identity ）、一个类型（type）和一个值（value）。

> Every object has an identity, a type and a value

标识：决定了object的唯一性，一般是内存地址，可用id()函数
类型：决定了object**有哪些方法**以及**能存什么样的值**，比如是否有length方法、是否能存数字；可用type()函数
值：object上存储的值，比如数字10

object的几个关键词：mutable（可修改）、immutable（不可修改）、 container（容器）

## 0x02: Python的内置类型

|类型|值|
|---|---|
|None|None|
|NotImplemented||
|Ellipsis|...|
|numbers.Number|Integral、Real、Complex|
|Sequences|Immutable:Strings、Tuples、Bytes; Mutable:Lists、Byte Arrays|
|Set|Sets、Frozen sets|
|Mappings|Dictionaries|
|Callable|User-defined functions、Instance methods、Generator functions、Coroutine functions、Asynchronous generator functions、Built-in functions、Built-in methods、Classes、Class Instances|
|Modules||
|Custom classes||
|Class instances||
| I/O objects||
|Internal types|Code objects、Methods on code objects、Frame objects、Traceback objects、Slice objects、Static method objects、Class method objects|

## 0x03. object上特殊的方法

|分类|名称|
|---|---|
|basic|object.\_\_new__、|