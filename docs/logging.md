# 日志处理

`logging` 模块是 Python 的标准日志库，提供了灵活的日志记录功能。

## 0x01. 基本使用

```python
import logging

# 基本配置
logging.basicConfig(level=logging.INFO)

# 日志级别（从低到高）
# DEBUG - 详细信息，通常仅在调试问题时使用
# INFO - 确认程序按预期工作
# WARNING - 表示发生了意外情况，但程序仍能工作
# ERROR - 由于更严重的问题，程序无法执行某些功能
# CRITICAL - 严重错误，程序可能无法继续运行

# 记录日志
logging.debug('这是调试信息')
logging.info('这是普通信息')
logging.warning('这是警告信息')
logging.error('这是错误信息')
logging.critical('这是严重错误信息')
```

## 0x02. 配置日志

### basicConfig 配置

```python
import logging

# 完整配置
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='app.log',
    filemode='w',  # 'w' 覆盖，'a' 追加
    encoding='utf-8'
)

logging.info('应用启动')
logging.error('发生错误')
```

### 格式化字符串

```python
import logging

# 可用的格式化字段
"""
%(asctime)s     - 日志时间
%(name)s        - Logger 名称
%(levelname)s   - 日志级别
%(message)s     - 日志消息
%(filename)s    - 文件名
%(lineno)d      - 行号
%(funcName)s    - 函数名
%(process)d     - 进程 ID
%(thread)d      - 线程 ID
%(pathname)s    - 完整文件路径
"""

# 自定义格式
formatter = logging.Formatter(
    '%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger('myapp')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.info('格式化日志示例')
# 输出: 2024-01-15 10:30:45 [INFO] example.py:15 - 格式化日志示例
```

## 0x03. Logger 和 Handler

### Logger 对象

```python
import logging

# 创建 logger
logger = logging.getLogger('myapp')
logger.setLevel(logging.DEBUG)

# 创建 handler
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('app.log')

# 设置 handler 级别
console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)

# 创建 formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 给 handler 添加 formatter
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 给 logger 添加 handler
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 使用 logger
logger.debug('这条只会记录到文件')
logger.info('这条会记录到文件和控制台')
logger.warning('警告信息')
```

### 多个 Logger

```python
import logging

# 不同模块使用不同的 logger
def setup_loggers():
    # 应用日志
    app_logger = logging.getLogger('app')
    app_logger.setLevel(logging.INFO)
    app_handler = logging.FileHandler('app.log')
    app_logger.addHandler(app_handler)
    
    # 数据库日志
    db_logger = logging.getLogger('app.database')
    db_logger.setLevel(logging.DEBUG)
    db_handler = logging.FileHandler('database.log')
    db_logger.addHandler(db_handler)
    
    # API 日志
    api_logger = logging.getLogger('app.api')
    api_logger.setLevel(logging.INFO)
    api_handler = logging.FileHandler('api.log')
    api_logger.addHandler(api_handler)

# 使用
app_logger = logging.getLogger('app')
db_logger = logging.getLogger('app.database')
api_logger = logging.getLogger('app.api')

app_logger.info('应用启动')
db_logger.debug('执行查询')
api_logger.info('API 请求')
```

## 0x04. 日志处理器

### 常用 Handler

```python
import logging
import logging.handlers

# StreamHandler - 输出到流（控制台）
console_handler = logging.StreamHandler()

# FileHandler - 输出到文件
file_handler = logging.FileHandler('app.log')

# RotatingFileHandler - 按大小轮转
rotating_handler = logging.handlers.RotatingFileHandler(
    'app.log',
    maxBytes=10*1024*1024,  # 10MB
    backupCount=5           # 保留5个备份
)

# TimedRotatingFileHandler - 按时间轮转
timed_handler = logging.handlers.TimedRotatingFileHandler(
    'app.log',
    when='midnight',    # 每天午夜轮转
    interval=1,         # 间隔1天
    backupCount=7       # 保留7天
)

# SMTPHandler - 发送邮件
email_handler = logging.handlers.SMTPHandler(
    mailhost=('smtp.example.com', 587),
    fromaddr='app@example.com',
    toaddrs=['admin@example.com'],
    subject='应用错误',
    credentials=('user', 'password'),
    secure=()
)

# HTTPHandler - 发送到 HTTP 服务器
http_handler = logging.handlers.HTTPHandler(
    host='log.example.com:8080',
    url='/log',
    method='POST'
)

# SysLogHandler - 系统日志
syslog_handler = logging.handlers.SysLogHandler(
    address='/dev/log'
)
```

### 过滤器

```python
import logging

class LevelFilter(logging.Filter):
    """只允许特定级别的日志"""
    def __init__(self, level):
        super().__init__()
        self.level = level
    
    def filter(self, record):
        return record.levelno == self.level

class KeywordFilter(logging.Filter):
    """根据关键词过滤"""
    def __init__(self, keyword):
        super().__init__()
        self.keyword = keyword
    
    def filter(self, record):
        return self.keyword not in record.getMessage()

# 使用过滤器
logger = logging.getLogger('myapp')

# 只记录 WARNING 级别
warning_filter = LevelFilter(logging.WARNING)
logger.addFilter(warning_filter)

# 过滤包含 "password" 的日志
password_filter = KeywordFilter('password')
logger.addFilter(password_filter)

logger.info('正常信息')          # 记录
logger.warning('警告信息')      # 记录
logger.info('用户密码已更改')   # 被过滤
```

## 0x05. 日志配置

### 使用配置文件

```python
# logging.conf
[loggers]
keys=root,myapp

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_myapp]
level=DEBUG
handlers=consoleHandler,fileHandler
qualName=myapp
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=INFO
formatter=simpleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=simpleFormatter
args=('app.log', 'a')

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=%Y-%m-%d %H:%M:%S
```

```python
import logging
import logging.config

# 加载配置文件
logging.config.fileConfig('logging.conf')

# 使用 logger
logger = logging.getLogger('myapp')
logger.info('从配置文件加载的日志')
```

### 使用字典配置

```python
import logging
import logging.config

config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'detailed': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': 'app.log',
            'maxBytes': 10485760,  # 10MB
            'backupCount': 5
        },
        'error_file': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'formatter': 'detailed',
            'filename': 'error.log'
        }
    },
    'loggers': {
        'myapp': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': False
        },
        'myapp.database': {
            'level': 'DEBUG',
            'handlers': ['file'],
            'propagate': False
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'error_file']
    }
}

# 应用配置
logging.config.dictConfig(config)

# 使用
logger = logging.getLogger('myapp')
logger.info('使用字典配置的日志')
```

## 0x06. 异常日志

```python
import logging

logger = logging.getLogger('myapp')

# 记录异常
try:
    result = 1 / 0
except ZeroDivisionError:
    logger.exception('发生除零错误')
    # exception() 自动包含异常堆栈信息

# 手动记录异常信息
try:
    result = int('abc')
except ValueError as e:
    logger.error('转换失败: %s', e, exc_info=True)

# 记录堆栈信息
def nested_function():
    logger.debug('在嵌套函数中')

def outer_function():
    logger.debug('在外部函数中')
    nested_function()

outer_function()
```

## 0x07. 实际应用

### 应用日志配置

```python
import logging
import logging.handlers
from pathlib import Path

def setup_logging(log_dir: str = 'logs', log_level: int = logging.INFO):
    """设置应用日志"""
    
    # 创建日志目录
    Path(log_dir).mkdir(exist_ok=True)
    
    # 配置
    config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
            'detailed': {
                'format': '%(asctime)s [%(levelname)s] %(name)s:%(funcName)s:%(lineno)d: %(message)s'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': log_level,
                'formatter': 'standard',
                'stream': 'ext://sys.stdout'
            },
            'file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': logging.DEBUG,
                'formatter': 'detailed',
                'filename': f'{log_dir}/app.log',
                'maxBytes': 10485760,
                'backupCount': 10
            },
            'error_file': {
                'class': 'logging.FileHandler',
                'level': logging.ERROR,
                'formatter': 'detailed',
                'filename': f'{log_dir}/error.log'
            }
        },
        'root': {
            'level': logging.DEBUG,
            'handlers': ['console', 'file', 'error_file']
        }
    }
    
    logging.config.dictConfig(config)

# 使用
setup_logging()
logger = logging.getLogger(__name__)

def main():
    logger.info('应用启动')
    try:
        # 应用逻辑
        pass
    except Exception:
        logger.exception('应用发生错误')
    finally:
        logger.info('应用退出')

if __name__ == '__main__':
    main()
```

### 装饰器记录日志

```python
import logging
import functools

logger = logging.getLogger(__name__)

def log_call(func):
    """记录函数调用的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug(f'调用 {func.__name__}，参数: args={args}, kwargs={kwargs}')
        try:
            result = func(*args, **kwargs)
            logger.debug(f'{func.__name__} 返回: {result}')
            return result
        except Exception as e:
            logger.error(f'{func.__name__} 发生异常: {e}')
            raise
    return wrapper

# 使用
@log_call
def add(a, b):
    return a + b

@log_call
def divide(a, b):
    return a / b

# 测试
add(1, 2)
try:
    divide(1, 0)
except ZeroDivisionError:
    pass
```

## 参考
1. [Python 官方文档 - logging](https://docs.python.org/3/library/logging.html)
2. [Python 官方文档 - logging HOWTO](https://docs.python.org/3/howto/logging.html)
3. [Python 官方文档 - logging 配置](https://docs.python.org/3/library/logging.config.html)