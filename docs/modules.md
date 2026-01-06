# 引入模块

在Python中，一个Module就是一个脚本文件。
文件的名称就是模块的名称，在其他脚本，或模块自身中，可以使用全局变量`__name__` 来获取到。

当直接运行一个脚本时，`__name__`会被设置成 `__main__`，这也是我们常看到Python程序的主入口函数中的这些代码
```python
if __name__ == '__main__':
    pass
```
这种方式，能让我们区分是被import导入的，还是被Python解释器直接运行的。

使用import关键字来导入module，导入后，以`moduleName.definitionName` 的方式来调用函数、变量、类名。

需要注意的是，以下划线`_` 开头的变量、函数，不会被导入。

module导入过程中，会从头到尾的运行一遍，所以，脚本里面定义的表达式、语句都会被执行。

import语句的几种写法

```python
# 可以直接 使用 模块中 函数、变量
from moduleName import fun1, fun2
from moduleName import *

# 给模块 起别名
import moduleName as mn
# 也可以给 导入的 变量、函数、类起别名
from moduleName import fun1 as fn
```

Python解释器搜索module的步骤：
1. 先搜索内置模块，可以使用`sys.builtin_module_names` 来查看
2. 搜索`sys.path` 变量给出的目录列表

而`sys.path` 变量从以下位置被初始化：
1. 执行Python命令的当前目录，或是输入脚本的目录
2. PYTHONPATH系统环境变量配置的目录列表，和配置Shell的PATH环境变量类似
3. 安装的依赖库，一般对应`site-package`目录，由site模块处理

分别打印一下上面提到的两个变量
```python
import sys

print(sys.builtin_module_names)
print(sys.path)
```
对于全局变量`sys.path`，可以像操作list一样的对其进行操作，如：
```python
import sys
sys.path.apend('/usr/local/python')
sys.path.insert(0, '..')
```

可以结合`dir()` 内置函数来查看module的目录

在Python中，包是一种用“点式模块名”构造 Python 模块命名空间的方法，可以把包理解成一个module集。

构建包的方法，是在一个目录中添加`__init__.py`文件，Python就会将该目录看成一个包。

在`__init__.py`里可以使用`__all__`变量声明导出哪些模块，以应对 `from...import *` 的模式

依然使用import语句，导入包
```python
# 直接导入p1包里的m2模块的fun1函数，这种方式，当用fun1函数时，要用全面，即 p1.m2.fun1
import p1.m2.fun1
# 起别名，就可以直接使用 fn
import p1.m2.fun1 as fn

# 使用from...import语句
# 从p1包里直接导入m2模块，可以直接使用 m2.fun1函数
from p1 import m2
# 从p1包里的m2模块中导入 fun1，这样可以直接使用fun1
from p1.m2 import fun1
```

对于同级包、上级包的导入，支持两种方式
```python
# 假如在p1.s1.m2模块中，使用p1.m2模块里的fun1函数
# 使用绝对 包名
from p1.m2 import fun1
# 使用相对路径
from .. import m2
```
使用相对路径时，注意`__main__`主文件入口的情况。

## 1 自带或第三方
安装相关模块后，直接 用 import导入即可

## 2 自定义模块
### 2.1 同级目录
直接 import 即可

### 2.2 子级目录
将子级目录做成 包，即，子级目录中加入 `__init__.py` 文件，其中，可以什么都不写，或者 导入目录中的全部模块

在父级目录中，可以直接使用 from、import 进行导入使用

### 2.3 父级目录
需要在 子级目录的模块中，添加
```python
import sys
sys.path.insert(0, '..')
```
然后，导入父级目录的模块，即可使用

如果调用同级目录的相关文件，需要将同级目录作为包的形式。