# collections 模块

`collections` 模块提供了额外的数据结构，扩展了 Python 内置的容器类型。

## 0x01. Counter - 计数器

`Counter` 用于统计可哈希对象的出现次数。

```python
from collections import Counter

# 从可迭代对象创建
c = Counter(['apple', 'banana', 'apple', 'cherry', 'banana', 'apple'])
print(c)  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# 从字典创建
c = Counter({'a': 3, 'b': 2, 'c': 1})
print(c)  # Counter({'a': 3, 'b': 2, 'c': 1})

# 从关键字参数创建
c = Counter(a=3, b=2, c=1)
print(c)  # Counter({'a': 3, 'b': 2, 'c': 1})

# 统计字符串中字符出现次数
c = Counter('abracadabra')
print(c)  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
```

### Counter 方法

```python
from collections import Counter

c = Counter(['apple', 'banana', 'apple', 'cherry', 'banana', 'apple'])

# 获取计数
print(c['apple'])    # 3
print(c['grape'])    # 0 (不存在的元素返回0)

# most_common - 获取最常见的元素
print(c.most_common(2))      # [('apple', 3), ('banana', 2)]
print(c.most_common())       # 所有元素按频率降序排列

# elements - 返回元素迭代器（重复元素按计数重复）
print(list(c.elements()))    # ['apple', 'apple', 'apple', 'banana', 'banana', 'cherry']

# total - 计算总数
print(c.total())  # 6

# 算术运算
c1 = Counter(a=3, b=2)
c2 = Counter(a=1, b=3)
print(c1 + c2)  # Counter({'a': 4, 'b': 5})
print(c1 - c2)  # Counter({'a': 2})  # 只保留正数
print(c1 & c2)  # Counter({'a': 1, 'b': 2})  # 交集（取最小值）
print(c1 | c2)  # Counter({'a': 3, 'b': 3})  # 并集（取最大值）

# update - 更新计数
c = Counter(a=1, b=2)
c.update(['a', 'a', 'b', 'c'])
print(c)  # Counter({'a': 3, 'b': 3, 'c': 1})

# subtract - 减去计数
c = Counter(a=3, b=2)
c.subtract(a=1, b=1, c=1)
print(c)  # Counter({'a': 2, 'b': 1, 'c': -1})
```

### 实际应用

```python
from collections import Counter

# 统计单词频率
text = "the quick brown fox jumps over the lazy dog the fox"
words = text.split()
word_count = Counter(words)
print(word_count.most_common(3))  # [('the', 3), ('fox', 2), ('quick', 1)]

# 统计列表中的重复元素
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
count = Counter(numbers)
duplicates = {k: v for k, v in count.items() if v > 1}
print(duplicates)  # {2: 2, 3: 3, 4: 4}

# 找出出现最多的元素
def most_frequent(lst):
    return Counter(lst).most_common(1)[0][0]

print(most_frequent([1, 2, 2, 3, 3, 3]))  # 3
```

## 0x02. defaultdict - 默认字典

`defaultdict` 为不存在的键提供默认值。

```python
from collections import defaultdict

# 使用 list 作为默认工厂
d = defaultdict(list)
d['fruits'].append('apple')
d['fruits'].append('banana')
d['vegetables'].append('carrot')
print(d)  # defaultdict(<class 'list'>, {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']})

# 使用 int 作为默认工厂（计数）
d = defaultdict(int)
for word in 'the quick brown fox'.split():
    d[word] += 1
print(d)  # defaultdict(<class 'int'>, {'the': 1, 'quick': 1, 'brown': 1, 'fox': 1})

# 使用 set 作为默认工厂
d = defaultdict(set)
d['colors'].add('red')
d['colors'].add('blue')
d['colors'].add('red')  # 重复添加无效
print(d['colors'])  # {'red', 'blue'}

# 使用自定义函数作为默认工厂
def default_value():
    return 'N/A'

d = defaultdict(default_value)
d['name'] = 'Alice'
print(d['name'])   # Alice
print(d['age'])    # N/A
```

### 实际应用

```python
from collections import defaultdict

# 分组
students = [
    {'name': 'Alice', 'grade': 'A'},
    {'name': 'Bob', 'grade': 'B'},
    {'name': 'Charlie', 'grade': 'A'},
    {'name': 'David', 'grade': 'B'},
    {'name': 'Eve', 'grade': 'A'},
]

groups = defaultdict(list)
for student in students:
    groups[student['grade']].append(student['name'])

print(dict(groups))  # {'A': ['Alice', 'Charlie', 'Eve'], 'B': ['Bob', 'David']}

# 构建邻接表
edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D')]
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

print(dict(graph))  # {'A': ['B', 'C'], 'B': ['A', 'C', 'D'], 'C': ['A', 'B'], 'D': ['B']}

# 统计多个列表中元素的出现次数
lists = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
count = defaultdict(int)
for lst in lists:
    for item in lst:
        count[item] += 1

print(dict(count))  # {1: 1, 2: 2, 3: 3, 4: 2, 5: 1}
```

## 0x03. OrderedDict - 有序字典

`OrderedDict` 保持插入顺序（Python 3.7+ 的普通字典也保持顺序）。

```python
from collections import OrderedDict

# 创建有序字典
od = OrderedDict()
od['banana'] = 3
od['apple'] = 1
od['cherry'] = 2
print(od)  # OrderedDict([('banana', 3), ('apple', 1), ('cherry', 2)])

# move_to_end - 移动元素到开头或结尾
od.move_to_end('apple')      # 移动到末尾
od.move_to_end('cherry', last=False)  # 移动到开头

# popitem - 弹出元素
od.popitem(last=True)   # 弹出最后一个元素
od.popitem(last=False)  # 弹出第一个元素

# 创建顺序字典（按特定顺序）
d = {'banana': 3, 'apple': 1, 'cherry': 2}
od = OrderedDict(sorted(d.items(), key=lambda x: x[1]))
print(od)  # OrderedDict([('apple', 1), ('cherry', 2), ('banana', 3)])
```

## 0x04. deque - 双端队列

`deque` 提供高效的两端添加和删除操作。

```python
from collections import deque

# 创建 deque
d = deque([1, 2, 3, 4, 5])
print(d)  # deque([1, 2, 3, 4, 5])

# 创建固定长度的 deque
d = deque(maxlen=5)
for i in range(7):
    d.append(i)
print(d)  # deque([2, 3, 4, 5, 6]) - 自动丢弃旧元素

# 添加元素
d.append(6)        # 右端添加
d.appendleft(0)    # 左端添加
print(d)  # deque([0, 1, 2, 3, 4, 5, 6])

d.extend([7, 8])   # 右端扩展
d.extendleft([-2, -1])  # 左端扩展（注意顺序）
print(d)  # deque([-1, -2, 0, 1, 2, 3, 4, 5, 6, 7, 8])

# 删除元素
d.pop()       # 右端删除
d.popleft()   # 左端删除

# 旋转
d = deque([1, 2, 3, 4, 5])
d.rotate(2)    # 向右旋转2步
print(d)  # deque([4, 5, 1, 2, 3])
d.rotate(-2)   # 向左旋转2步
print(d)  # deque([1, 2, 3, 4, 5])

# 计数和查找
print(d.count(3))  # 1
d.remove(3)        # 删除第一个匹配的元素
```

### 实际应用

```python
from collections import deque

# 滑动窗口
def sliding_window(iterable, n):
    """返回滑动窗口的迭代器"""
    it = iter(iterable)
    window = deque(maxlen=n)
    for item in it:
        window.append(item)
        if len(window) == n:
            yield tuple(window)

# 使用
data = [1, 2, 3, 4, 5, 6, 7]
for window in sliding_window(data, 3):
    print(window)
# (1, 2, 3)
# (2, 3, 4)
# (3, 4, 5)
# (4, 5, 6)
# (5, 6, 7)

# BFS 广度优先搜索
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph.get(node, []))
    
    return result

# 使用
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}
print(bfs(graph, 'A'))  # ['A', 'B', 'C', 'D', 'E']

# 最近 N 个元素
class RecentHistory:
    def __init__(self, max_size=10):
        self.history = deque(maxlen=max_size)
    
    def add(self, item):
        self.history.append(item)
    
    def get_recent(self, n=None):
        if n is None:
            return list(self.history)
        return list(self.history)[-n:]

# 使用
history = RecentHistory(5)
for i in range(7):
    history.add(i)
print(history.get_recent())  # [2, 3, 4, 5, 6]
print(history.get_recent(3)) # [4, 5, 6]
```

## 0x05. namedtuple - 命名元组

`namedtuple` 创建带有字段名称的元组子类。

```python
from collections import namedtuple

# 创建 namedtuple 类
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, 22)
print(p)        # Point(x=11, y=22)
print(p.x, p.y)  # 11 22

# 多种创建方式
Point = namedtuple('Point', 'x, y')
Point = namedtuple('Point', 'x y')

# 使用关键字参数创建
p = Point(x=11, y=22)

# 访问元素
print(p[0])      # 11 (索引访问)
print(p.x)       # 11 (属性访问)

# 元组解包
x, y = p
print(f'x={x}, y={y}')

# 转换为字典
print(p._asdict())  # {'x': 11, 'y': 22}

# 创建新实例（修改字段）
p2 = p._replace(x=33)
print(p2)  # Point(x=33, y=22)

# 获取字段名
print(Point._fields)  # ('x', 'y')
```

### 实际应用

```python
from collections import namedtuple

# 数据记录
Employee = namedtuple('Employee', ['name', 'age', 'department', 'salary'])
emp = Employee('Alice', 30, 'Engineering', 100000)
print(f'{emp.name} 在 {emp.department} 部门')

# 颜色表示
Color = namedtuple('Color', ['red', 'green', 'blue'])
red = Color(255, 0, 0)
green = Color(0, 255, 0)

# 坐标
Coordinate = namedtuple('Coordinate', ['latitude', 'longitude'])
beijing = Coordinate(39.9042, 116.4074)
shanghai = Coordinate(31.2304, 121.4737)

# 数据库记录
User = namedtuple('User', ['id', 'name', 'email', 'created_at'])
users = [
    User(1, 'Alice', 'alice@example.com', '2024-01-01'),
    User(2, 'Bob', 'bob@example.com', '2024-01-02'),
]

# 从字典创建
data = {'name': 'Charlie', 'age': 25, 'department': 'HR', 'salary': 80000}
emp = Employee(**data)
print(emp)

# 嵌套 namedtuple
Address = namedtuple('Address', ['street', 'city', 'country'])
Person = namedtuple('Person', ['name', 'age', 'address'])

addr = Address('123 Main St', 'Beijing', 'China')
person = Person('Alice', 30, addr)
print(f'{person.name} 住在 {person.address.city}')
```

## 0x06. ChainMap - 链式映射

`ChainMap` 将多个字典组合成一个可更新的视图。

```python
from collections import ChainMap

# 创建 ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
cm = ChainMap(dict1, dict2)
print(cm)  # ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})

# 查找（从第一个字典开始）
print(cm['a'])  # 1
print(cm['b'])  # 2 (来自 dict1)
print(cm['c'])  # 4

# 获取所有键
print(list(cm.keys()))    # ['b', 'c', 'a']
print(list(cm.values()))  # [3, 4, 1]

# 新的子上下文
cm = cm.new_child({'d': 5})
print(cm['d'])  # 5

# 实际应用：配置管理
defaults = {'theme': 'light', 'language': 'en', 'font_size': 12}
user_prefs = {'theme': 'dark', 'font_size': 14}
cmd_args = {'language': 'zh'}

config = ChainMap(cmd_args, user_prefs, defaults)
print(config['theme'])      # dark
print(config['language'])   # zh
print(config['font_size'])  # 14
print(config.get('unknown', 'default'))  # default
```

## 0x07. UserDict, UserList, UserString

这些类用于创建自定义容器类。

```python
from collections import UserDict

# 自定义字典
class CaseInsensitiveDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)
    
    def __getitem__(self, key):
        return super().__getitem__(key.lower())

d = CaseInsensitiveDict()
d['Name'] = 'Alice'
d['AGE'] = 30
print(d['name'])  # Alice
print(d['age'])   # 30

from collections import UserList

# 自定义列表
class SortedList(UserList):
    def append(self, item):
        super().append(item)
        self.data.sort()

sl = SortedList()
sl.append(3)
sl.append(1)
sl.append(2)
print(sl)  # [1, 2, 3]

from collections import UserString

# 自定义字符串
class UpperString(UserString):
    def __init__(self, string):
        super().__init__(string.upper())

s = UpperString('hello')
print(s)  # HELLO
```

## 参考
1. [Python 官方文档 - collections](https://docs.python.org/3/library/collections.html)
2. [Python 官方文档 - Counter](https://docs.python.org/3/library/collections.html#collections.Counter)
3. [Python 官方文档 - defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict)
4. [Python 官方文档 - deque](https://docs.python.org/3/library/collections.html#collections.deque)