# 异常处理

异常是程序运行时发生的错误，Python 提供了完善的异常处理机制来优雅地处理这些错误。

## 0x01. 常见异常类型

```python
# 常见内置异常
# SyntaxError - 语法错误
# IndentationError - 缩进错误
# NameError - 变量名未定义
# TypeError - 类型错误
# ValueError - 值错误
# IndexError - 索引越界
# KeyError - 字典键不存在
# AttributeError - 属性不存在
# FileNotFoundError - 文件未找到
# ZeroDivisionError - 除零错误
# ImportError - 导入错误
# IOError - 输入输出错误
# RuntimeError - 运行时错误
# MemoryError - 内存错误

# 示例
# print(undefined_variable)  # NameError
# int('abc')                  # ValueError
# [1, 2, 3][10]               # IndexError
# {'a': 1}['b']               # KeyError
```

## 0x02. 基本异常处理

### try-except

```python
# 基本语法
try:
    result = 10 / 0
except ZeroDivisionError:
    print('不能除以零')

# 捕获异常对象
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f'错误类型: {type(e).__name__}')
    print(f'错误信息: {e}')

# 捕获多种异常
try:
    value = int(input('请输入数字: '))
    result = 10 / value
except ValueError:
    print('输入的不是有效数字')
except ZeroDivisionError:
    print('不能除以零')

# 合并捕获多种异常
try:
    value = int(input('请输入数字: '))
    result = 10 / value
except (ValueError, ZeroDivisionError) as e:
    print(f'发生错误: {e}')
```

### try-except-else

```python
# else 块在没有异常时执行
try:
    number = int('42')
except ValueError:
    print('转换失败')
else:
    print(f'转换成功: {number}')

# 实际应用
def read_number(filename):
    try:
        with open(filename, 'r') as f:
            number = int(f.read())
    except FileNotFoundError:
        print(f'文件 {filename} 不存在')
        return None
    except ValueError:
        print('文件内容不是有效数字')
        return None
    else:
        return number
```

### try-except-finally

```python
# finally 块总是执行，用于清理资源
try:
    file = open('data.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print('文件不存在')
finally:
    # 无论是否发生异常，都会执行
    print('清理操作')
    if 'file' in locals():
        file.close()

# 完整结构
try:
    result = 10 / 0
except ZeroDivisionError:
    print('捕获到异常')
else:
    print('没有异常')
finally:
    print('总是执行')
```

## 0x03. 主动抛出异常

### raise 语句

```python
# 抛出内置异常
def set_age(age):
    if age < 0:
        raise ValueError('年龄不能为负数')
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f'错误: {e}')

# 抛出带附加信息的异常
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError(f'不能将 {a} 除以零')
    return a / b

try:
    divide(10, 0)
except ZeroDivisionError as e:
    print(e)

# 重新抛出异常
def process_data(data):
    try:
        result = int(data)
    except ValueError:
        print('记录错误日志')
        raise  # 重新抛出当前异常
    return result
```

### 自定义异常

```python
# 定义自定义异常类
class CustomError(Exception):
    """自定义异常基类"""
    pass

class ValidationError(CustomError):
    """验证错误"""
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f'{field}: {message}')

class BusinessError(CustomError):
    """业务逻辑错误"""
    def __init__(self, code, message):
        self.code = code
        self.message = message
        super().__init__(f'[{code}] {message}')

# 使用自定义异常
def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError('age', '必须是整数')
    if age < 0 or age > 150:
        raise ValidationError('age', '必须在0-150之间')
    return age

def create_order(user_id, amount):
    if amount <= 0:
        raise BusinessError('ORDER_001', '订单金额必须大于0')
    # 创建订单逻辑
    pass

# 捕获自定义异常
try:
    validate_age(-5)
except ValidationError as e:
    print(f'验证失败: {e}')
    print(f'字段: {e.field}')

try:
    create_order(1, -100)
except BusinessError as e:
    print(f'业务错误: {e}')
    print(f'错误代码: {e.code}')
```

## 0x04. 异常链

```python
# 使用 from 保留原始异常
def connect_database():
    try:
        # 模拟数据库连接失败
        raise ConnectionError('数据库连接失败')
    except ConnectionError as e:
        raise RuntimeError('无法初始化应用') from e

try:
    connect_database()
except RuntimeError as e:
    print(f'错误: {e}')
    print(f'原始错误: {e.__cause__}')

# 隐藏原始异常
def safe_operation():
    try:
        result = 1 / 0
    except ZeroDivisionError:
        raise ValueError('计算错误') from None

try:
    safe_operation()
except ValueError as e:
    print(f'错误: {e}')
    # 不会显示原始的 ZeroDivisionError
```

## 0x05. 异常最佳实践

### 异常处理原则

```python
# 1. 只捕获你知道如何处理的异常
# 好的做法
try:
    data = json.loads(json_string)
except json.JSONDecodeError:
    print('JSON格式错误')

# 不好的做法（捕获所有异常）
try:
    data = json.loads(json_string)
except:
    pass

# 2. 使用具体的异常类型
# 好的做法
try:
    value = int(string_value)
except ValueError:
    print('转换失败')

# 不好的做法
try:
    value = int(string_value)
except:
    print('出错了')

# 3. 不要用异常控制正常流程
# 不好的做法
def get_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return None

# 好的做法
def get_value(dictionary, key):
    return dictionary.get(key)

# 4. 记录异常信息
import logging

logging.basicConfig(level=logging.ERROR)

try:
    result = 1 / 0
except ZeroDivisionError:
    logging.exception('发生除零错误')
    # 或者
    logging.error('计算错误', exc_info=True)
```

### 上下文管理器与异常

```python
# with 语句自动处理异常时的清理
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
    
    def __enter__(self):
        print(f'连接到数据库 {self.db_name}')
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'关闭数据库连接')
        if exc_type:
            print(f'发生异常: {exc_val}')
        return False  # 不抑制异常

# 使用
with DatabaseConnection('mydb') as db:
    # 即使发生异常，连接也会被正确关闭
    raise ValueError('模拟错误')
```

## 0x06. 常见异常处理模式

### 重试机制

```python
import time

def retry(func, max_attempts=3, delay=1):
    """重试装饰器"""
    def wrapper(*args, **kwargs):
        for attempt in range(max_attempts):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt == max_attempts - 1:
                    raise
                print(f'尝试 {attempt + 1} 失败: {e}')
                time.sleep(delay)
    return wrapper

@retry(max_attempts=3, delay=1)
def fetch_data(url):
    # 模拟网络请求
    import random
    if random.random() < 0.7:
        raise ConnectionError('网络错误')
    return {'data': 'success'}

# 使用
try:
    result = fetch_data('http://example.com')
    print(result)
except ConnectionError:
    print('所有重试都失败了')
```

### 异常转换

```python
# 将底层异常转换为高层异常
class DatabaseError(Exception):
    pass

def query_user(user_id):
    try:
        # 模拟数据库查询
        if user_id <= 0:
            raise ValueError('无效的用户ID')
        return {'id': user_id, 'name': 'Alice'}
    except ValueError as e:
        raise DatabaseError(f'查询用户失败: {e}') from e
    except ConnectionError as e:
        raise DatabaseError(f'数据库连接失败: {e}') from e

# 使用
try:
    user = query_user(-1)
except DatabaseError as e:
    print(f'数据库错误: {e}')
```

### 异常收集

```python
def process_batch(items):
    """处理批量数据，收集所有错误"""
    errors = []
    results = []
    
    for item in items:
        try:
            result = process_item(item)
            results.append(result)
        except Exception as e:
            errors.append({
                'item': item,
                'error': str(e),
                'type': type(e).__name__
            })
    
    return results, errors

def process_item(item):
    if item < 0:
        raise ValueError(f'负数不允许: {item}')
    return item ** 2

# 使用
items = [1, -2, 3, -4, 5]
results, errors = process_batch(items)
print(f'成功: {results}')
print(f'失败: {errors}')
```

### 可选返回值

```python
from typing import Optional, Tuple

def safe_divide(a: float, b: float) -> Tuple[Optional[float], Optional[str]]:
    """安全除法，返回结果和错误信息"""
    try:
        return a / b, None
    except ZeroDivisionError:
        return None, '除数不能为零'

# 使用
result, error = safe_divide(10, 0)
if error:
    print(f'错误: {error}')
else:
    print(f'结果: {result}')

# 或者使用 dataclass
from dataclasses import dataclass
from typing import Any

@dataclass
class Result:
    success: bool
    data: Any = None
    error: str = None

def safe_operation(value):
    try:
        return Result(success=True, data=int(value))
    except ValueError as e:
        return Result(success=False, error=str(e))

# 使用
result = safe_operation('abc')
if result.success:
    print(f'数据: {result.data}')
else:
    print(f'错误: {result.error}')
```

## 参考
1. [Python 官方文档 - 异常](https://docs.python.org/3/tutorial/errors.html)
2. [Python 官方文档 - 内置异常](https://docs.python.org/3/library/exceptions.html)
3. [PEP 3134 - 异常链](https://peps.python.org/pep-3134/)