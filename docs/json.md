# JSON 处理

JSON（JavaScript Object Notation）是一种轻量级的数据交换格式，Python 提供了内置的 `json` 模块来处理 JSON 数据。

## 0x01. 基本使用

### Python 与 JSON 类型对应

```python
"""
Python 类型       JSON 类型
-----------      ---------
dict             object
list, tuple      array
str              string
int, float       number
True             true
False            false
None             null
"""

import json

# Python 数据
data = {
    'name': 'Alice',
    'age': 25,
    'scores': [90, 85, 92],
    'active': True,
    'address': None
}

# 编码为 JSON 字符串
json_str = json.dumps(data)
print(json_str)
# {"name": "Alice", "age": 25, "scores": [90, 85, 92], "active": true, "address": null}

# 解码为 Python 对象
python_obj = json.loads(json_str)
print(python_obj)
# {'name': 'Alice', 'age': 25, 'scores': [90, 85, 92], 'active': True, 'address': None}
```

### 文件操作

```python
import json

# 写入 JSON 文件
data = {'name': 'Alice', 'age': 25}
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 读取 JSON 文件
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)
```

## 0x02. 格式化输出

```python
import json

data = {
    'name': 'Alice',
    'age': 25,
    'scores': [90, 85, 92],
    'address': {
        'city': '北京',
        'street': '中关村'
    }
}

# 缩进格式化
print(json.dumps(data, indent=2))

# 自定义缩进和分隔符
print(json.dumps(data, indent=4, separators=(',', ': ')))

# 排序键
print(json.dumps(data, indent=2, sort_keys=True))

# 中文处理
print(json.dumps(data, ensure_ascii=False, indent=2))
# {"name": "Alice", "age": 25, "address": {"city": "北京", ...}}
```

## 0x03. 编码选项

```python
import json
from datetime import datetime
from decimal import Decimal

# 自定义编码器
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, set):
            return list(obj)
        return super().default(obj)

# 使用自定义编码器
data = {
    'time': datetime.now(),
    'price': Decimal('19.99'),
    'tags': {'python', 'json'}
}

json_str = json.dumps(data, cls=CustomEncoder, indent=2)
print(json_str)

# 使用 default 参数
def custom_encoder(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f'Object of type {type(obj)} is not JSON serializable')

json_str = json.dumps(data, default=custom_encoder)
```

## 0x04. 解码选项

```python
import json
from datetime import datetime

# 自定义解码
json_str = '{"time": "2024-01-15T10:30:00", "name": "Alice"}'

def custom_decoder(obj):
    for key, value in obj.items():
        if key == 'time':
            obj[key] = datetime.fromisoformat(value)
    return obj

data = json.loads(json_str, object_hook=custom_decoder)
print(data['time'])  # 2024-01-15 10:30:00

# 使用 object_pairs_hook
def handle_duplicates(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            if isinstance(result[key], list):
                result[key].append(value)
            else:
                result[key] = [result[key], value]
        else:
            result[key] = value
    return result

json_str = '{"a": 1, "a": 2, "b": 3}'
data = json.loads(json_str, object_pairs_hook=handle_duplicates)
print(data)  # {'a': [1, 2], 'b': 3}

# 解析类
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f'User(name={self.name}, age={self.age})'

def decode_user(obj):
    if 'name' in obj and 'age' in obj:
        return User(obj['name'], obj['age'])
    return obj

json_str = '{"name": "Alice", "age": 25}'
user = json.loads(json_str, object_hook=decode_user)
print(user)  # User(name=Alice, age=25)
```

## 0x05. 处理大型 JSON

### 流式处理

```python
import json

# 按行读取 JSON（JSON Lines 格式）
def read_json_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                yield json.loads(line)

# 使用
for record in read_json_lines('data.jsonl'):
    print(record)

# 写入 JSON Lines
def write_json_lines(filename, records):
    with open(filename, 'w', encoding='utf-8') as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + '\n')

# 使用
records = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
]
write_json_lines('output.jsonl', records)
```

### 增量解析

```python
import json
from json import JSONDecoder, JSONDecodeError

def decode_json_objects(json_str):
    """解析多个 JSON 对象"""
    decoder = JSONDecoder()
    pos = 0
    while pos < len(json_str):
        try:
            obj, end = decoder.raw_decode(json_str, pos)
            yield obj
            pos = end
        except JSONDecodeError:
            pos += 1

# 使用
json_str = '{"a": 1} {"b": 2} {"c": 3}'
for obj in decode_json_objects(json_str):
    print(obj)
```

## 0x06. 实用工具

### JSON 比较

```python
import json

def compare_json(json1, json2):
    """比较两个 JSON 对象"""
    if type(json1) != type(json2):
        return False
    
    if isinstance(json1, dict):
        if set(json1.keys()) != set(json2.keys()):
            return False
        return all(compare_json(json1[k], json2[k]) for k in json1)
    
    if isinstance(json1, list):
        if len(json1) != len(json2):
            return False
        return all(compare_json(a, b) for a, b in zip(json1, json2))
    
    return json1 == json2

# 使用
data1 = {'a': 1, 'b': [2, 3]}
data2 = {'a': 1, 'b': [2, 3]}
data3 = {'a': 1, 'b': [2, 4]}

print(compare_json(data1, data2))  # True
print(compare_json(data1, data3))  # False
```

### JSON 路径查询

```python
import json
from typing import Any

def get_by_path(data: Any, path: str, default=None):
    """通过路径获取值
    路径格式: 'key1.key2[0].key3'
    """
    keys = path.replace('[', '.[').split('.')
    current = data
    
    for key in keys:
        if key.startswith('[') and key.endswith(']'):
            # 数组索引
            try:
                index = int(key[1:-1])
                current = current[index]
            except (ValueError, IndexError, TypeError):
                return default
        else:
            # 字典键
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return default
    
    return current

# 使用
data = {
    'users': [
        {'name': 'Alice', 'scores': [90, 85]},
        {'name': 'Bob', 'scores': [88, 92]}
    ]
}

print(get_by_path(data, 'users[0].name'))       # Alice
print(get_by_path(data, 'users[1].scores[0]'))   # 88
print(get_by_path(data, 'users[2].name', 'N/A')) # N/A
```

### JSON 转换

```python
import json
from collections import OrderedDict

def flatten_json(data, parent_key='', sep='.'):
    """展平嵌套 JSON"""
    items = []
    if isinstance(data, dict):
        for k, v in data.items():
            new_key = f'{parent_key}{sep}{k}' if parent_key else k
            items.extend(flatten_json(v, new_key, sep).items())
    elif isinstance(data, list):
        for i, v in enumerate(data):
            new_key = f'{parent_key}{sep}{i}' if parent_key else str(i)
            items.extend(flatten_json(v, new_key, sep).items())
    else:
        items.append((parent_key, data))
    return dict(items)

def unflatten_json(data, sep='.'):
    """还原展平的 JSON"""
    result = {}
    for key, value in data.items():
        parts = key.split(sep)
        current = result
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
        current[parts[-1]] = value
    return result

# 使用
nested = {
    'user': {
        'name': 'Alice',
        'address': {
            'city': 'Beijing'
        }
    }
}

flat = flatten_json(nested)
print(flat)
# {'user.name': 'Alice', 'user.address.city': 'Beijing'}

original = unflatten_json(flat)
print(original)
# {'user': {'name': 'Alice', 'address': {'city': 'Beijing'}}}
```

## 0x07. 配置管理

```python
import json
from pathlib import Path
from typing import Any, Dict

class JSONConfig:
    """JSON 配置文件管理器"""
    
    def __init__(self, config_path: str):
        self.config_path = Path(config_path)
        self.config: Dict[str, Any] = {}
        self.load()
    
    def load(self):
        """加载配置"""
        if self.config_path.exists():
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
    
    def save(self):
        """保存配置"""
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)
    
    def get(self, key: str, default=None):
        """获取配置值"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value
    
    def set(self, key: str, value: Any):
        """设置配置值"""
        keys = key.split('.')
        config = self.config
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        config[keys[-1]] = value
        self.save()

# 使用
config = JSONConfig('config.json')
config.set('database.host', 'localhost')
config.set('database.port', 5432)

print(config.get('database.host'))  # localhost
print(config.get('database.port'))  # 5432
```

## 参考
1. [Python 官方文档 - json](https://docs.python.org/3/library/json.html)
2. [JSON 官方网站](https://www.json.org/)
3. [JSON Lines 格式](https://jsonlines.org/)