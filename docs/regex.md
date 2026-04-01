# 正则表达式

正则表达式（Regular Expression）是一种强大的文本匹配和处理工具。

## 0x01. 基本使用

```python
import re

# 基本匹配
text = 'Hello, World!'
pattern = r'Hello'
result = re.search(pattern, text)
print(result)  # <re.Match object; span=(0, 5), match='Hello'>

# 匹配失败返回 None
pattern = r'Python'
result = re.search(pattern, text)
print(result)  # None

# 原始字符串 r'' 避免转义
pattern = r'\d+'  # 匹配数字
pattern = '\\d+'  # 等价，但不推荐
```

## 0x02. 常用函数

### search - 搜索匹配

```python
import re

text = 'The price is 42 dollars'

# search - 搜索第一个匹配
match = re.search(r'\d+', text)
if match:
    print(f'找到: {match.group()}')    # 找到: 42
    print(f'位置: {match.span()}')     # 位置: (14, 16)
    print(f'起始: {match.start()}')    # 起始: 14
    print(f'结束: {match.end()}')      # 结束: 16
```

### match - 从开头匹配

```python
import re

# match - 从字符串开头匹配
text = 'Hello, World!'
print(re.match(r'Hello', text))   # 匹配成功
print(re.match(r'World', text))   # 匹配失败（不在开头）

# 等价于 search + ^
print(re.search(r'^World', text))  # 匹配失败
```

### findall - 查找所有匹配

```python
import re

text = 'The price is 42 and quantity is 100'

# findall - 返回所有匹配的列表
numbers = re.findall(r'\d+', text)
print(numbers)  # ['42', '100']

# 带分组的 findall
text = 'John: 25, Alice: 30, Bob: 28'
pairs = re.findall(r'(\w+): (\d+)', text)
print(pairs)  # [('John', '25'), ('Alice', '30'), ('Bob', '28')]
```

### finditer - 迭代所有匹配

```python
import re

text = 'The price is 42 and quantity is 100'

# finditer - 返回匹配对象的迭代器
for match in re.finditer(r'\d+', text):
    print(f'{match.group()} at {match.span()}')
# 42 at (14, 16)
# 100 at (33, 36)
```

### sub - 替换

```python
import re

text = 'The price is 42 dollars'

# sub - 替换匹配
result = re.sub(r'\d+', 'NUMBER', text)
print(result)  # The price is NUMBER dollars

# 使用函数替换
def double(match):
    return str(int(match.group()) * 2)

result = re.sub(r'\d+', double, text)
print(result)  # The price is 84 dollars

# 替换次数
text = '1 2 3 4 5'
result = re.sub(r'\d+', 'X', text, count=2)
print(result)  # X X 3 4 5
```

### split - 分割

```python
import re

# 按多个分隔符分割
text = 'one,two;three four.five'
parts = re.split(r'[,;.\s]+', text)
print(parts)  # ['one', 'two', 'three', 'four', 'five']

# 保留分隔符（使用分组）
parts = re.split(r'([,;.\s]+)', text)
print(parts)  # ['one', ',', 'two', ';', 'three', ' ', 'four', '.', 'five']

# 限制分割次数
parts = re.split(r'\s+', 'a b c d e', maxsplit=2)
print(parts)  # ['a', 'b', 'c d e']
```

## 0x03. 元字符

```python
import re

"""
基本元字符
.   - 匹配任意字符（除换行符）
^   - 匹配字符串开头
$   - 匹配字符串结尾
*   - 匹配前一个字符0次或多次
+   - 匹配前一个字符1次或多次
?   - 匹配前一个字符0次或1次
\   - 转义字符
|   - 或运算
()  - 分组
[]  - 字符类
{}  - 重复次数
"""

# . 匹配任意字符
print(re.search(r'h.t', 'hat'))   # hat
print(re.search(r'h.t', 'hot'))   # hot
print(re.search(r'h.t', 'hit'))   # hit

# ^ 和 $
print(re.search(r'^Hello', 'Hello World'))   # 匹配
print(re.search(r'World$', 'Hello World'))   # 匹配

# * + ?
print(re.findall(r'ab*', 'a ab abb abbb'))   # ['a', 'ab', 'abb', 'abbb']
print(re.findall(r'ab+', 'a ab abb abbb'))   # ['ab', 'abb', 'abbb']
print(re.findall(r'ab?', 'a ab abb abbb'))   # ['a', 'ab', 'ab', 'ab']

# |
print(re.findall(r'cat|dog', 'I have a cat and a dog'))  # ['cat', 'dog']

# ()
match = re.match(r'(\d{4})-(\d{2})-(\d{2})', '2024-01-15')
print(match.groups())  # ('2024', '01', '15')
print(match.group(1))  # 2024
print(match.group(2))  # 01
print(match.group(3))  # 15
```

## 0x04. 字符类

```python
import re

"""
字符类
[abc]   - 匹配 a 或 b 或 c
[^abc]  - 匹配除 a, b, c 之外的字符
[a-z]   - 匹配 a 到 z
[A-Z]   - 匹配 A 到 Z
[0-9]   - 匹配 0 到 9
[a-zA-Z0-9] - 匹配字母或数字

预定义字符类
\d  - 数字 [0-9]
\D  - 非数字 [^0-9]
\w  - 单词字符 [a-zA-Z0-9_]
\W  - 非单词字符
\s  - 空白字符 [ \t\n\r\f\v]
\S  - 非空白字符
\b  - 单词边界
\B  - 非单词边界
"""

# 字符类
print(re.findall(r'[aeiou]', 'hello'))    # ['e', 'o']
print(re.findall(r'[^aeiou]', 'hello'))   # ['h', 'l', 'l']
print(re.findall(r'[a-z]', 'Hello123'))   # ['e', 'l', 'l', 'o']
print(re.findall(r'[0-9]', 'Hello123'))   # ['1', '2', '3']

# 预定义字符类
print(re.findall(r'\d+', 'abc 123 def 456'))  # ['123', '456']
print(re.findall(r'\w+', 'Hello, World!'))    # ['Hello', 'World']
print(re.findall(r'\s+', 'Hello   World'))    # ['   ']

# 单词边界
text = 'cat concatenate category'
print(re.findall(r'\bcat\b', text))  # ['cat'] 只匹配完整单词
```

## 0x05. 量词

```python
import re

"""
量词
*       - 0 次或多次 (贪婪)
+       - 1 次或多次 (贪婪)
?       - 0 次或 1 次 (贪婪)
{n}     - 恰好 n 次
{n,}    - 至少 n 次
{n,m}   - n 到 m 次

非贪婪量词
*?      - 0 次或多次 (非贪婪)
+?      - 1 次或多次 (非贪婪)
??      - 0 次或 1 次 (非贪婪)
{n,m}?  - n 到 m 次 (非贪婪)
"""

# 贪婪 vs 非贪婪
html = '<b>Bold</b> and <i>Italic</i>'

# 贪婪匹配（尽可能多）
print(re.findall(r'<.*>', html))   # ['<b>Bold</b> and <i>Italic</i>']

# 非贪婪匹配（尽可能少）
print(re.findall(r'<.*?>', html))  # ['<b>', '</b>', '<i>', '</i>']

# 具体次数
print(re.findall(r'\d{3}', '12345678'))   # ['123', '456']
print(re.findall(r'\d{2,4}', '1 12 123 1234 12345'))
# ['12', '123', '1234', '12', '345']
print(re.findall(r'\d{2,}', '1 12 123 1234'))
# ['12', '123', '1234']
```

## 0x06. 分组和引用

```python
import re

# 捕获分组
match = re.match(r'(\w+) (\w+)', 'Hello World')
print(match.group(0))  # Hello World (整个匹配)
print(match.group(1))  # Hello (第一组)
print(match.group(2))  # World (第二组)
print(match.groups())  # ('Hello', 'World')

# 命名分组
match = re.match(r'(?P<first>\w+) (?P<last>\w+)', 'Hello World')
print(match.group('first'))  # Hello
print(match.group('last'))   # World
print(match.groupdict())     # {'first': 'Hello', 'last': 'World'}

# 反向引用
text = 'Hello Hello World World'
# \1 引用第一个分组
result = re.sub(r'(\w+) \1', r'\1', text)
print(result)  # Hello World

# 使用命名反向引用
result = re.sub(r'(?P<word>\w+) (?P=word)', r'\g<word>', text)
print(result)  # Hello World

# 非捕获分组 (?:...)
text = 'http://example.com https://example.org'
# (?:...) 不捕获，只分组
matches = re.findall(r'(?:http|https)://(\w+\.\w+)', text)
print(matches)  # ['example.com', 'example.org']

# 前瞻 (?=...) 和后顾 (?<=...)
text = '100 dollars 50 euros 30 pounds'
# 前瞻：后面是 dollars 的数字
print(re.findall(r'\d+(?= dollars)', text))  # ['100']
# 后顾：前面是 $ 的数字
text = '$100 €50 £30'
print(re.findall(r'(?<=\$)\d+', text))  # ['100']
# 否定前瞻 (?!...)
print(re.findall(r'\d+(?! dollars)', '100 dollars 50 euros'))  # ['50']
# 否定后顾 (?<!...)
print(re.findall(r'(?<!\$)\d+', '$100 50'))  # ['100', '50']
```

## 0x07. 编译正则表达式

```python
import re

# 预编译正则表达式（提高效率）
pattern = re.compile(r'\d+')
print(pattern.findall('abc 123 def 456'))  # ['123', '456']
print(pattern.search('abc 123'))           # <re.Match object>

# 编译时指定标志
pattern = re.compile(r'hello', re.IGNORECASE)
print(pattern.findall('Hello HELLO hello'))  # ['Hello', 'HELLO', 'hello']

# 多行模式
text = '''line1
line2
line3'''
pattern = re.compile(r'^line\d', re.MULTILINE)
print(pattern.findall(text))  # ['line1', 'line2', 'line3']

# 详细模式（忽略空白和注释）
pattern = re.compile(r'''
    \d+     # 数字
    \.      # 小数点
    \d+     # 小数部分
''', re.VERBOSE)
print(pattern.findall('3.14 2.71'))  # ['3.14', '2.71']
```

## 0x08. 常用标志

```python
import re

"""
re.IGNORECASE (re.I) - 忽略大小写
re.MULTILINE (re.M)  - 多行模式（^$ 匹配每行）
re.DOTALL (re.S)     - . 匹配包括换行符
re.VERBOSE (re.X)    - 详细模式（允许注释和空白）
re.ASCII (re.A)      - ASCII 模式
re.DEBUG             - 显示调试信息
"""

# IGNORECASE
print(re.findall(r'hello', 'Hello HELLO', re.IGNORECASE))
# ['Hello', 'HELLO']

# MULTILINE
text = '''line1
line2
line3'''
print(re.findall(r'^line', text, re.MULTILINE))
# ['line', 'line', 'line']

# DOTALL
text = '''line1
line2'''
print(re.findall(r'line1.*line2', text, re.DOTALL))
# ['line1\nline2']

# 组合标志
pattern = re.compile(r'hello', re.IGNORECASE | re.MULTILINE)
```

## 0x09. 实际应用

### 验证输入

```python
import re

def validate_email(email):
    """验证邮箱格式"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone):
    """验证手机号格式（中国）"""
    pattern = r'^1[3-9]\d{9}$'
    return bool(re.match(pattern, phone))

def validate_url(url):
    """验证 URL 格式"""
    pattern = r'^https?://[^\s/$.?#].[^\s]*$'
    return bool(re.match(pattern, url))

def validate_ip(ip):
    """验证 IP 地址格式"""
    pattern = r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$'
    return bool(re.match(pattern, ip))

# 测试
print(validate_email('test@example.com'))  # True
print(validate_phone('13812345678'))       # True
print(validate_url('https://example.com')) # True
print(validate_ip('192.168.1.1'))          # True
```

### 文本处理

```python
import re

def extract_emails(text):
    """提取文本中的邮箱"""
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

def extract_urls(text):
    """提取文本中的 URL"""
    pattern = r'https?://[^\s]+'
    return re.findall(pattern, text)

def extract_hashtags(text):
    """提取话题标签"""
    pattern = r'#\w+'
    return re.findall(pattern, text)

def mask_sensitive_info(text):
    """脱敏敏感信息"""
    # 手机号脱敏
    text = re.sub(r'(1[3-9]\d)\d{4}(\d{4})', r'\1****\2', text)
    # 邮箱脱敏
    text = re.sub(r'(\w{3})\w+@', r'\1***@', text)
    # 身份证脱敏
    text = re.sub(r'(\d{4})\d{10}(\d{4})', r'\1**********\2', text)
    return text

# 测试
text = '联系邮箱: test@example.com, 电话: 13812345678'
print(extract_emails(text))  # ['test@example.com']
print(mask_sensitive_info(text))
# 联系邮箱: tes***@example.com, 电话: 138****5678
```

### 数据提取

```python
import re

def parse_log(log_line):
    """解析日志行"""
    pattern = r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] (\w+) (.+)'
    match = re.match(pattern, log_line)
    if match:
        return {
            'timestamp': match.group(1),
            'level': match.group(2),
            'message': match.group(3)
        }
    return None

def extract_table_data(html):
    """提取 HTML 表格数据"""
    rows = re.findall(r'<tr>(.*?)</tr>', html, re.DOTALL)
    data = []
    for row in rows:
        cells = re.findall(r'<td>(.*?)</td>', row)
        data.append(cells)
    return data

# 测试
log = '[2024-01-15 10:30:45] ERROR Database connection failed'
print(parse_log(log))
# {'timestamp': '2024-01-15 10:30:45', 'level': 'ERROR', 'message': 'Database connection failed'}
```

## 参考
1. [Python 官方文档 - re 模块](https://docs.python.org/3/library/re.html)
2. [Python 正则表达式 HOWTO](https://docs.python.org/3/howto/regex.html)
3. [正则表达式在线测试](https://regex101.com/)