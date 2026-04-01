# 处理字符串

字符串是 Python 中最常用的数据类型之一，用于表示文本信息。

## 0x01. 创建字符串

Python 中可以使用单引号、双引号或三引号创建字符串。

```python
# 单引号
s1 = 'hello world'

# 双引号
s2 = "hello world"

# 三引号：用于多行字符串
s3 = '''这是一个
多行字符串'''

s4 = """另一个
多行字符串"""

# 原始字符串（不转义）
path = r'C:\Users\name\Documents'
print(path)  # C:\Users\name\Documents

# 转义字符
print('hello\nworld')  # 换行
print('hello\tworld')  # 制表符
print('hello\'world')  # 转义单引号
print('hello\\world')  # 转义反斜杠
```

## 0x02. f-string 格式化

Python 3.6+ 引入的 f-string 提供了简洁的字符串格式化方式。

```python
name = 'Alice'
age = 25
score = 95.5

# 基本用法
greeting = f'Hello, {name}! You are {age} years old.'
print(greeting)  # Hello, Alice! You are 25 years old.

# 表达式
print(f'{name} will be {age + 1} next year.')  # Alice will be 26 next year.

# 数字格式化
print(f'Score: {score:.1f}')  # Score: 95.5
print(f'Pi: {3.14159:.2f}')   # Pi: 3.14

# 对齐和填充
print(f'{"left":<10}')    # left      (左对齐)
print(f'{"right":>10}')   #      right (右对齐)
print(f'{"center":^10}')  #   center   (居中)
print(f'{"hello":*^10}')  # **hello*** (填充字符)

# 千位分隔符
print(f'{1234567:,}')     # 1,234,567
print(f'{1234567:,.2f}')  # 1,234,567.00

# 日期格式化
from datetime import datetime
now = datetime.now()
print(f'{now:%Y-%m-%d %H:%M:%S}')  # 2024-01-01 12:30:45
```

## 0x03. r-string 原始字符串

原始字符串不处理转义字符，常用于正则表达式和文件路径。

```python
# 文件路径
path = r'C:\Users\name\Documents\file.txt'
print(path)  # C:\Users\name\Documents\file.txt

# 正则表达式
import re
pattern = r'\d+'
result = re.findall(pattern, 'There are 3 cats and 4 dogs')
print(result)  # ['3', '4']

# 对比：非原始字符串需要双反斜杠
path2 = 'C:\\Users\\name\\Documents\\file.txt'
print(path2 == path)  # True
```

## 0x04. 字符串操作

### 索引和切片

```python
s = 'Hello, World!'

# 索引（从 0 开始）
print(s[0])    # 'H'
print(s[-1])   # '!'
print(s[-2])   # 'd'

# 切片 [start:stop:step]
print(s[0:5])   # 'Hello'
print(s[7:])    # 'World!'
print(s[:5])    # 'Hello'
print(s[::2])   # 'Hlo ol!'
print(s[::-1])  # '!dlroW ,olleH' (反转字符串)
```

### 字符串拼接和重复

```python
# 拼接
s1 = 'Hello'
s2 = 'World'
s3 = s1 + ', ' + s2 + '!'
print(s3)  # Hello, World!

# 重复
s4 = 'ha' * 3
print(s4)  # 'hahaha'

# join 方法（推荐用于大量字符串拼接）
words = ['Python', 'is', 'awesome']
sentence = ' '.join(words)
print(sentence)  # 'Python is awesome'

# 字符串拼接性能比较
import time

# 慢：每次拼接创建新字符串
start = time.time()
result = ''
for i in range(10000):
    result += str(i)
slow_time = time.time() - start

# 快：使用 join
start = time.time()
result = ''.join(str(i) for i in range(10000))
fast_time = time.time() - start

print(f'Slow: {slow_time:.4f}s, Fast: {fast_time:.4f}s')
```

### 字符串查找

```python
s = 'Hello, World!'

# find() 和 index()
print(s.find('World'))     # 7 (找到返回索引)
print(s.find('Python'))    # -1 (未找到返回 -1)
print(s.index('World'))    # 7 (找到返回索引)
# print(s.index('Python')) # ValueError (未找到抛出异常)

# rfind() 和 rindex()：从右侧开始查找
s2 = 'Hello, Hello, Hello!'
print(s2.rfind('Hello'))   # 14

# count()：统计出现次数
print(s2.count('Hello'))   # 3

# startswith() 和 endswith()
print(s.startswith('Hello'))  # True
print(s.endswith('!'))        # True
```

### 字符串替换

```python
s = 'Hello, World!'

# replace()：替换所有匹配项
new_s = s.replace('World', 'Python')
print(new_s)  # Hello, Python!

# 限制替换次数
s2 = 'aaa bbb aaa ccc aaa'
new_s2 = s2.replace('aaa', 'xxx', 2)
print(new_s2)  # xxx bbb xxx ccc aaa

# translate()：使用映射表替换
table = str.maketrans('aeiou', '12345')
print('hello'.translate(table))  # 'h2ll4'
```

### 字符串分割

```python
s = 'Hello, World!'

# split()：按分隔符分割
words = s.split(' ')
print(words)  # ['Hello,', 'World!']

# 限制分割次数
parts = 'a-b-c-d-e'.split('-', 2)
print(parts)  # ['a', 'b', 'c-d-e']

# splitlines()：按行分割
text = '''line1
line2
line3'''
lines = text.splitlines()
print(lines)  # ['line1', 'line2', 'line3']

# partition()：分割成三部分
before, sep, after = 'Hello-World'.partition('-')
print(before)  # 'Hello'
print(sep)     # '-'
print(after)   # 'World'
```

### 字符串大小写转换

```python
s = 'Hello, World!'

print(s.upper())      # 'HELLO, WORLD!'
print(s.lower())      # 'hello, world!'
print(s.title())      # 'Hello, World!'
print(s.capitalize()) # 'Hello, world!'
print(s.swapcase())   # 'hELLO, wORLD!'
```

### 字符串判断

```python
# 字符类型判断
print('hello'.isalpha())    # True (全是字母)
print('123'.isdigit())      # True (全是数字)
print('hello123'.isalnum()) # True (字母或数字)
print('   '.isspace())      # True (全是空白)
print('Hello'.isupper())    # False (全是大写)
print('hello'.islower())    # True (全是小写)
print('Hello'.istitle())    # True (标题格式)

# 前缀和后缀判断
print('Hello'.startswith('He'))  # True
print('Hello'.endswith('lo'))    # True
```

### 字符串填充和对齐

```python
# 居中填充
print('hello'.center(11, '*'))  # ***hello***

# 左填充
print('42'.zfill(5))            # '00042'
print('42'.rjust(5, '0'))       # '00042'

# 右填充
print('hello'.ljust(10, '-'))   # 'hello-----'

# 去除空白
s = '   hello   '
print(s.strip())    # 'hello'
print(s.lstrip())   # 'hello   '
print(s.rstrip())   # '   hello'

# 去除指定字符
s2 = '###hello###'
print(s2.strip('#'))  # 'hello'
```

## 0x05. 字符串编码和解码

```python
# 字符串编码为字节
text = '你好，世界'
encoded = text.encode('utf-8')
print(encoded)  # b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c'

# 字节解码为字符串
decoded = encoded.decode('utf-8')
print(decoded)  # '你好，世界'

# 其他编码方式
gbk_encoded = text.encode('gbk')
print(gbk_encoded)

# 编码错误处理
try:
    '你好'.encode('ascii')
except UnicodeEncodeError as e:
    print(f'编码错误: {e}')

# 使用 errors 参数处理错误
print('你好'.encode('ascii', errors='ignore'))     # b''
print('你好'.encode('ascii', errors='replace'))    # b'??'
print('你好'.encode('ascii', errors='xmlcharrefreplace'))  # b'&#20320;&#22909;'
```

## 0x06. 字符串格式化（其他方式）

除了 f-string，还有其他格式化方式：

```python
# % 格式化（旧式）
name = 'Alice'
age = 25
print('Hello, %s! You are %d years old.' % (name, age))

# format() 方法
print('Hello, {}! You are {} years old.'.format(name, age))
print('Hello, {0}! You are {1} years old.'.format(name, age))
print('Hello, {name}! You are {age} years old.'.format(name=name, age=age))

# 模板字符串
from string import Template
t = Template('Hello, $name! You are $age years old.')
print(t.substitute(name=name, age=age))
```

## 0x07. 字符串常量

```python
import string

# 字母
print(string.ascii_letters)  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.ascii_lowercase) # 'abcdefghijklmnopqrstuvwxyz'
print(string.ascii_uppercase) # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 数字
print(string.digits)          # '0123456789'

# 标点符号
print(string.punctuation)     # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# 空白字符
print(string.whitespace)      # ' \t\n\r\x0b\x0c'
```

## 0x08. 正则表达式基础

```python
import re

text = 'Contact us at info@example.com or support@example.com'

# 查找所有邮箱地址
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(pattern, text)
print(emails)  # ['info@example.com', 'support@example.com']

# 搜索第一个匹配
match = re.search(r'\d+', 'There are 42 cats')
if match:
    print(match.group())  # '42'

# 替换
new_text = re.sub(r'\d+', 'NUMBER', 'There are 42 cats and 13 dogs')
print(new_text)  # 'There are NUMBER cats and NUMBER dogs'

# 分割
parts = re.split(r'\s+', 'Hello   World   Python')
print(parts)  # ['Hello', 'World', 'Python']
```

## 参考
1. [Python 官方文档 - 字符串方法](https://docs.python.org/3/library/stdtypes.html#string-methods)
2. [Python 官方文档 - 格式化字符串](https://docs.python.org/3/library/string.html)
3. [Python 官方文档 - 正则表达式](https://docs.python.org/3/library/re.html)