# 如何处理文件？

Python 提供了丰富的文件操作功能，支持文本文件、二进制文件、JSON、CSV 等多种格式。

## 0x01. 基本文件操作

使用内置函数 `open()` 来读取一个文件，open函数会返回一个`fileObject`对象。

### 打开文件

```python
# 以文本模式打开文件（默认）
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 以二进制模式打开文件
with open('image.png', 'rb') as f:
    binary_data = f.read()

# 打开模式说明
# 'r'  - 只读（默认）
# 'w'  - 写入（覆盖）
# 'a'  - 追加
# 'x'  - 独占创建
# 'b'  - 二进制模式
# 't'  - 文本模式（默认）
# '+'  - 读写模式
```

### 读取文件

```python
# 读取整个文件
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

# 逐行读取
with open('file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())  # strip() 去除换行符

# 读取所有行到列表
with open('file.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)  # ['line1\n', 'line2\n', 'line3\n']

# 读取一行
with open('file.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    print(line)
```

### 写入文件

```python
# 写入文本
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, World!\n')
    f.write('第二行\n')

# 写入多行
lines = ['第一行\n', '第二行\n', '第三行\n']
with open('output.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)

# 追加模式
with open('output.txt', 'a', encoding='utf-8') as f:
    f.write('追加的内容\n')
```

### 文件指针操作

```python
# tell() - 获取当前位置
with open('file.txt', 'r') as f:
    print(f.tell())  # 0
    f.read(10)
    print(f.tell())  # 10

# seek() - 移动指针
with open('file.txt', 'r') as f:
    f.seek(0)   # 移动到开头
    f.seek(10)  # 移动到第10个字节
    f.seek(0, 2)  # 移动到文件末尾
```

## 0x02. os.path 模块

```python
import os.path

# 路径操作
path = '/home/user/documents/file.txt'

print(os.path.abspath('file.txt'))      # 获取绝对路径
print(os.path.basename(path))           # 'file.txt'
print(os.path.dirname(path))            # '/home/user/documents'
print(os.path.splitext(path))           # ('/home/user/documents/file', '.txt')
print(os.path.join('/home', 'user', 'file.txt'))  # '/home/user/file.txt'

# 路径判断
print(os.path.exists(path))             # 判断是否存在
print(os.path.isfile(path))             # 判断是否是文件
print(os.path.isdir(path))              # 判断是否是目录
print(os.path.isabs(path))              # 判断是否是绝对路径

# 获取文件信息
print(os.path.getsize(path))            # 获取文件大小（字节）
print(os.path.getmtime(path))           # 获取修改时间
```

## 0x03. os 模块

```python
import os

# 目录操作
os.getcwd()                    # 获取当前工作目录
os.chdir('/path/to/dir')       # 改变当前目录
os.listdir('.')                # 列出目录内容
os.mkdir('new_dir')            # 创建目录
os.makedirs('a/b/c')           # 递归创建目录
os.rmdir('dir')                # 删除空目录
os.removedirs('a/b/c')         # 递归删除空目录

# 文件操作
os.rename('old.txt', 'new.txt')  # 重命名
os.remove('file.txt')            # 删除文件

# 遍历目录
for root, dirs, files in os.walk('.'):
    for file in files:
        print(os.path.join(root, file))

# 环境变量
print(os.environ.get('HOME'))
os.environ['MY_VAR'] = 'value'
```

## 0x04. pathlib 模块（Python 3.4+）

```python
from pathlib import Path

# 创建路径对象
p = Path('.')
p = Path('/home/user/documents')
p = Path('file.txt')

# 路径操作
print(p.name)           # 文件名
print(p.stem)           # 文件名（不含扩展名）
print(p.suffix)         # 扩展名
print(p.parent)         # 父目录
print(p.parents)        # 所有父目录
print(p.absolute())     # 绝对路径

# 路径拼接
p = Path('/home') / 'user' / 'file.txt'
print(p)  # /home/user/file.txt

# 路径判断
print(p.exists())       # 是否存在
print(p.is_file())      # 是否是文件
print(p.is_dir())       # 是否是目录

# 文件操作
p.read_text(encoding='utf-8')        # 读取文本
p.read_bytes()                       # 读取二进制
p.write_text('Hello')                # 写入文本
p.write_bytes(b'binary data')        # 写入二进制

# 目录操作
Path('new_dir').mkdir(exist_ok=True)  # 创建目录
Path('new_dir').mkdir(parents=True, exist_ok=True)  # 递归创建

# 遍历目录
for file in Path('.').rglob('*.py'):  # 递归查找所有 .py 文件
    print(file)

for file in Path('.').iterdir():      # 列出目录内容
    print(file)
```

## 0x05. JSON 文件处理

```python
import json

# 写入 JSON
data = {
    'name': 'Alice',
    'age': 25,
    'scores': [85, 90, 78],
    'address': {
        'city': 'Beijing',
        'zip': '100000'
    }
}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# 读取 JSON
with open('data.json', 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)
    print(loaded_data)

# JSON 字符串转换
json_str = json.dumps(data, indent=2, ensure_ascii=False)
print(json_str)

parsed = json.loads(json_str)
print(parsed)
```

## 0x06. CSV 文件处理

```python
import csv

# 写入 CSV
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'Beijing'],
    ['Bob', 30, 'Shanghai'],
    ['Charlie', 35, 'Guangzhou']
]

with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# 读取 CSV
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 使用 DictReader/DictWriter
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['Name'], row['Age'])
```

## 0x07. YAML 文件处理

```python
# 需要安装 PyYAML: pip install pyyaml
import yaml

# 写入 YAML
data = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'name': 'mydb'
    },
    'users': ['alice', 'bob', 'charlie']
}

with open('config.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(data, f, default_flow_style=False)

# 读取 YAML
with open('config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)
    print(config)
```

## 0x08. 临时文件

```python
import tempfile
import os

# 创建临时文件
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
    f.write('临时数据')
    temp_path = f.name

# 使用后删除
os.unlink(temp_path)

# 创建临时目录
with tempfile.TemporaryDirectory() as temp_dir:
    # 在临时目录中操作
    temp_file = os.path.join(temp_dir, 'test.txt')
    with open(temp_file, 'w') as f:
        f.write('测试')
    # 退出 with 块后自动删除

# 获取系统临时目录
print(tempfile.gettempdir())
```

## 0x09. 文件编码检测

```python
# 使用 chardet 检测编码
# pip install chardet
import chardet

with open('unknown_encoding.txt', 'rb') as f:
    raw_data = f.read()
    result = chardet.detect(raw_data)
    print(result)  # {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

    # 使用检测到的编码读取
    encoding = result['encoding']
    text = raw_data.decode(encoding)
```

## 0x0A. 压缩文件处理

```python
import zipfile
import tarfile

# ZIP 文件
# 创建 ZIP
with zipfile.ZipFile('archive.zip', 'w') as zf:
    zf.write('file1.txt')
    zf.write('file2.txt')

# 读取 ZIP
with zipfile.ZipFile('archive.zip', 'r') as zf:
    print(zf.namelist())  # 列出文件
    zf.extractall('output_dir')  # 解压所有文件
    content = zf.read('file1.txt')  # 读取特定文件

# TAR 文件
# 创建 TAR
with tarfile.open('archive.tar.gz', 'w:gz') as tf:
    tf.add('file1.txt')
    tf.add('directory')

# 读取 TAR
with tarfile.open('archive.tar.gz', 'r:gz') as tf:
    tf.extractall('output_dir')
```

## 参考
1. [Python 官方文档 - 文件和目录访问](https://docs.python.org/3/library/filesys.html)
2. [Python 官方文档 - pathlib](https://docs.python.org/3/library/pathlib.html)
3. [Python 官方文档 - json](https://docs.python.org/3/library/json.html)
4. [Python 官方文档 - csv](https://docs.python.org/3/library/csv.html)