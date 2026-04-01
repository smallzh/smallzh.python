# 上下文管理器

上下文管理器（Context Manager）用于自动管理资源的获取和释放，确保代码块执行前后正确处理资源。

## 0x01. with 语句

### 基本使用

```python
# 文件操作 - 自动关闭文件
with open('file.txt', 'r') as f:
    content = f.read()
# 文件自动关闭，即使发生异常

# 多个上下文管理器
with open('input.txt', 'r') as f_in, open('output.txt', 'w') as f_out:
    f_out.write(f_in.read())

# Python 3.10+ 括号形式
with (
    open('input.txt', 'r') as f_in,
    open('output.txt', 'w') as f_out
):
    f_out.write(f_in.read())
```

## 0x02. 实现上下文管理器

### 类实现

```python
class DatabaseConnection:
    """数据库连接上下文管理器"""
    
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
    
    def __enter__(self):
        """进入上下文时调用"""
        print(f'连接到数据库: {self.connection_string}')
        self.connection = {'status': 'connected'}
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文时调用
        
        参数:
        - exc_type: 异常类型（如果没有异常则为 None）
        - exc_val: 异常值
        - exc_tb: 异常追踪信息
        
        返回:
        - True: 抑制异常
        - False: 传播异常
        """
        print('关闭数据库连接')
        self.connection = None
        
        if exc_type:
            print(f'发生异常: {exc_val}')
        
        return False  # 不抑制异常

# 使用
with DatabaseConnection('localhost:5432/mydb') as conn:
    print(f'连接状态: {conn["status"]}')
    # 模拟操作
    # raise ValueError('模拟错误')  # 测试异常处理
```

### 函数实现（contextmanager）

```python
from contextlib import contextmanager

@contextmanager
def timer():
    """计时器上下文管理器"""
    import time
    start = time.perf_counter()
    try:
        yield  # 这里是 with 块的代码
    finally:
        end = time.perf_counter()
        print(f'耗时: {end - start:.4f} 秒')

# 使用
with timer():
    # 模拟耗时操作
    sum(range(1000000))

@contextmanager
def temporary_directory():
    """临时目录上下文管理器"""
    import tempfile
    import shutil
    from pathlib import Path
    
    temp_dir = Path(tempfile.mkdtemp())
    try:
        yield temp_dir
    finally:
        shutil.rmtree(temp_dir)

# 使用
with temporary_directory() as temp_dir:
    # 在临时目录中操作
    (temp_dir / 'test.txt').write_text('hello')
    print(f'临时目录: {temp_dir}')
# 临时目录自动删除
```

## 0x03. 常用上下文管理器

### 文件操作

```python
# 基本文件操作
with open('file.txt', 'r') as f:
    content = f.read()

# 写入文件
with open('file.txt', 'w') as f:
    f.write('Hello, World!')

# 追加模式
with open('file.txt', 'a') as f:
    f.write('\nNew line')
```

### 锁

```python
import threading

# 线程锁
lock = threading.Lock()

with lock:
    # 临界区代码
    print('获得锁')

# RLock - 可重入锁
rlock = threading.RLock()

with rlock:
    with rlock:  # 可以多次获取
        print('重入锁')
```

### 临时文件

```python
import tempfile

# 临时文件
with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
    f.write('临时内容')
    temp_path = f.name
print(f'临时文件路径: {temp_path}')

# 临时目录
with tempfile.TemporaryDirectory() as temp_dir:
    print(f'临时目录: {temp_dir}')
    # 目录自动删除
```

### 数据库连接

```python
import sqlite3

# SQLite 连接
with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    results = cursor.fetchall()
# 自动提交或回滚
```

### 网络连接

```python
import socket

# Socket 连接
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('example.com', 80))
    s.send(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')
    response = s.recv(4096)
# 自动关闭连接
```

## 0x04. 高级用法

### 嵌套上下文管理器

```python
from contextlib import contextmanager

@contextmanager
def database_transaction(connection):
    """数据库事务上下文管理器"""
    cursor = connection.cursor()
    try:
        yield cursor
        connection.commit()
        print('事务提交')
    except Exception:
        connection.rollback()
        print('事务回滚')
        raise
    finally:
        cursor.close()

@contextmanager
def database_connection(db_path):
    """数据库连接上下文管理器"""
    import sqlite3
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    finally:
        conn.close()

# 嵌套使用
with database_connection('test.db') as conn:
    with database_transaction(conn) as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY)')
        cursor.execute('INSERT INTO test VALUES (1)')
```

### 条件上下文管理器

```python
from contextlib import contextmanager, ExitStack

@contextmanager
def conditional_context(condition, context_manager):
    """条件上下文管理器"""
    if condition:
        with context_manager as value:
            yield value
    else:
        yield None

# 使用
debug_mode = True
with conditional_context(debug_mode, open('debug.log', 'w')) as log_file:
    if log_file:
        log_file.write('调试信息')
    else:
        print('调试模式关闭')

# ExitStack - 动态管理多个上下文
with ExitStack() as stack:
    files = [
        stack.enter_context(open(f'file{i}.txt', 'w'))
        for i in range(3)
    ]
    for i, f in enumerate(files):
        f.write(f'文件 {i}')
```

### 异常处理上下文

```python
from contextlib import contextmanager, suppress

# suppress - 抑制特定异常
with suppress(FileNotFoundError):
    import os
    os.remove('nonexistent.txt')
# 不会抛出异常

@contextmanager
def error_handler(error_type, handler):
    """自定义异常处理"""
    try:
        yield
    except error_type as e:
        handler(e)

# 使用
def handle_value_error(e):
    print(f'处理错误: {e}')

with error_handler(ValueError, handle_value_error):
    raise ValueError('测试错误')
```

## 0x05. 实际应用

### 性能监控

```python
from contextlib import contextmanager
import time
import functools

@contextmanager
def performance_monitor(name):
    """性能监控上下文管理器"""
    import psutil
    import os
    
    process = psutil.Process(os.getpid())
    
    start_time = time.perf_counter()
    start_memory = process.memory_info().rss
    
    try:
        yield
    finally:
        end_time = time.perf_counter()
        end_memory = process.memory_info().rss
        
        print(f'[{name}] 耗时: {end_time - start_time:.4f} 秒')
        print(f'[{name}] 内存变化: {(end_memory - start_memory) / 1024 / 1024:.2f} MB')

# 使用
with performance_monitor('数据处理'):
    data = [i ** 2 for i in range(1000000)]
```

### 配置管理

```python
from contextlib import contextmanager
import os

@contextmanager
def environment_variable(key, value):
    """临时设置环境变量"""
    old_value = os.environ.get(key)
    os.environ[key] = value
    try:
        yield
    finally:
        if old_value is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = old_value

@contextmanager
def working_directory(path):
    """临时切换工作目录"""
    old_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old_dir)

# 使用
with environment_variable('DEBUG', 'true'):
    print(f'DEBUG={os.environ.get("DEBUG")}')

with working_directory('/tmp'):
    print(f'当前目录: {os.getcwd()}')
```

### 资源池

```python
from contextlib import contextmanager
from queue import Queue
import threading

class ResourcePool:
    """资源池"""
    
    def __init__(self, max_size=5):
        self.pool = Queue(max_size)
        self.lock = threading.Lock()
        self.created = 0
        self.max_size = max_size
    
    def _create_resource(self):
        """创建资源"""
        self.created += 1
        return f'Resource-{self.created}'
    
    @contextmanager
    def acquire(self):
        """获取资源"""
        try:
            resource = self.pool.get_nowait()
        except:
            with self.lock:
                if self.created < self.max_size:
                    resource = self._create_resource()
                else:
                    resource = self.pool.get()
        
        try:
            yield resource
        finally:
            self.pool.put(resource)

# 使用
pool = ResourcePool(3)

def worker(pool, worker_id):
    with pool.acquire() as resource:
        print(f'Worker {worker_id} 使用 {resource}')

threads = [threading.Thread(target=worker, args=(pool, i)) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
```

### 缓存上下文

```python
from contextlib import contextmanager
from functools import lru_cache

@contextmanager
def cache_enabled(maxsize=128):
    """启用缓存的上下文管理器"""
    original_functions = {}
    
    def enable_cache(func):
        original_functions[func.__name__] = func
        return lru_cache(maxsize=maxsize)(func)
    
    try:
        yield enable_cache
    finally:
        # 清理缓存
        for func in original_functions.values():
            if hasattr(func, 'cache_clear'):
                func.cache_clear()

# 使用
def expensive_calculation(n):
    print(f'计算 {n}...')
    return sum(range(n))

with cache_enabled() as cache:
    cached_calc = cache(expensive_calculation)
    print(cached_calc(1000000))  # 第一次计算
    print(cached_calc(1000000))  # 使用缓存
```

## 参考
1. [Python 官方文档 - with 语句](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)
2. [Python 官方文档 - contextlib](https://docs.python.org/3/library/contextlib.html)
3. [PEP 343 - with 语句](https://peps.python.org/pep-0343/)