# 迭代器和生成器

## 迭代器
### 以类的方式使用
类内部定义`__iter__`和`__next__`方法
```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
for it in rev:
    print(it)
```

### 以函数的方式使用
内部函数
iter()
next()
```python
s = 'abc'
it = iter(s)
next(it)
next(it)
```

## 生成器 和生成器表达式
### 生成器
yeid 关键字
```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)
```
### 生成器表达式
```python
sum(i*i for i in range(10))                 # sum of squares

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))         # dot product

unique_words = set(word for line in page  for word in line.split())

valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))
```

## 列表推导式