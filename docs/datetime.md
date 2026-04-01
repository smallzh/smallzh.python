# 日期和时间处理

Python 提供了多个模块来处理日期和时间，主要包括 `datetime`、`time` 和 `calendar`。

## 0x01. datetime 模块

### 基本类型

```python
from datetime import datetime, date, time, timedelta

# date - 日期
today = date.today()
print(f'今天: {today}')  # 2024-01-15
print(f'年: {today.year}, 月: {today.month}, 日: {today.day}')

# time - 时间
t = time(14, 30, 45)
print(f'时间: {t}')  # 14:30:45
print(f'时: {t.hour}, 分: {t.minute}, 秒: {t.second}')

# datetime - 日期和时间
now = datetime.now()
print(f'现在: {now}')  # 2024-01-15 14:30:45.123456

# 创建特定日期时间
dt = datetime(2024, 1, 15, 14, 30, 45)
print(f'指定时间: {dt}')

# timedelta - 时间差
delta = timedelta(days=7, hours=3, minutes=30)
print(f'时间差: {delta}')  # 7 days, 3:30:00
```

### 日期时间运算

```python
from datetime import datetime, timedelta

now = datetime.now()

# 日期加减
tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)
next_week = now + timedelta(weeks=1)
next_hour = now + timedelta(hours=1)

print(f'明天: {tomorrow}')
print(f'昨天: {yesterday}')
print(f'下周: {next_week}')

# 计算时间差
start = datetime(2024, 1, 1)
end = datetime(2024, 12, 31)
diff = end - start
print(f'天数差: {diff.days}')  # 365

# 比较日期
date1 = datetime(2024, 1, 15)
date2 = datetime(2024, 1, 20)
print(f'date1 < date2: {date1 < date2}')  # True
print(f'date1 == date2: {date1 == date2}')  # False

# 替换日期时间部分
now = datetime.now()
new_time = now.replace(hour=0, minute=0, second=0)
print(f'午夜: {new_time}')
```

### 日期格式化

```python
from datetime import datetime

now = datetime.now()

# strftime - 格式化为字符串
print(now.strftime('%Y-%m-%d'))           # 2024-01-15
print(now.strftime('%Y/%m/%d %H:%M:%S'))  # 2024/01/15 14:30:45
print(now.strftime('%Y年%m月%d日'))        # 2024年01月15日
print(now.strftime('%A, %B %d, %Y'))      # Monday, January 15, 2024

# strptime - 从字符串解析
date_str = '2024-01-15'
dt = datetime.strptime(date_str, '%Y-%m-%d')
print(f'解析结果: {dt}')

date_str = '2024年01月15日 14:30:45'
dt = datetime.strptime(date_str, '%Y年%m月%d日 %H:%M:%S')
print(f'解析结果: {dt}')
```

### 常用格式代码

```python
"""
%Y - 四位年份 (2024)
%y - 两位年份 (24)
%m - 月份 (01-12)
%d - 日期 (01-31)
%H - 24小时制小时 (00-23)
%I - 12小时制小时 (01-12)
%M - 分钟 (00-59)
%S - 秒 (00-59)
%f - 微秒 (000000-999999)
%a - 星期缩写 (Mon)
%A - 星期全称 (Monday)
%b - 月份缩写 (Jan)
%B - 月份全称 (January)
%p - AM/PM
%j - 年中第几天 (001-366)
%U - 年中第几周 (00-53)
%w - 星期几 (0-6, 0是星期日)
%Z - 时区名称
%% - 字面 %
"""
```

## 0x02. 时区处理

### 使用 zoneinfo (Python 3.9+)

```python
from datetime import datetime
from zoneinfo import ZoneInfo

# 获取当前时间（带时区）
utc_now = datetime.now(ZoneInfo('UTC'))
print(f'UTC 时间: {utc_now}')

# 转换时区
beijing_tz = ZoneInfo('Asia/Shanghai')
beijing_time = utc_now.astimezone(beijing_tz)
print(f'北京时间: {beijing_time}')

# 创建带时区的时间
dt = datetime(2024, 1, 15, 14, 30, tzinfo=beijing_tz)
print(f'带时区的时间: {dt}')

# 转换到不同时区
tokyo_tz = ZoneInfo('Asia/Tokyo')
tokyo_time = dt.astimezone(tokyo_tz)
print(f'东京时间: {tokyo_time}')

# 常用时区
# 'UTC' - 协调世界时
# 'Asia/Shanghai' - 中国标准时间
# 'Asia/Tokyo' - 日本标准时间
# 'America/New_York' - 美国东部时间
# 'Europe/London' - 英国时间
```

### 使用 pytz (兼容旧版本)

```python
# pip install pytz
import pytz
from datetime import datetime

# 获取时区
beijing_tz = pytz.timezone('Asia/Shanghai')
utc_tz = pytz.UTC

# 创建带时区的时间
utc_now = datetime.now(utc_tz)
print(f'UTC 时间: {utc_now}')

# 转换时区
beijing_time = utc_now.astimezone(beijing_tz)
print(f'北京时间: {beijing_time}')

# 创建本地时间并本地化
local_dt = datetime(2024, 1, 15, 14, 30)
localized_dt = beijing_tz.localize(local_dt)
print(f'本地化时间: {localized_dt}')

# 列出所有时区
# for tz in pytz.all_timezones:
#     print(tz)
```

## 0x03. time 模块

```python
import time

# 获取当前时间戳
timestamp = time.time()
print(f'当前时间戳: {timestamp}')  # 1705312245.123456

# 时间戳转本地时间
local_time = time.localtime(timestamp)
print(f'本地时间: {time.strftime("%Y-%m-%d %H:%M:%S", local_time)}')

# 时间戳转 UTC 时间
utc_time = time.gmtime(timestamp)
print(f'UTC 时间: {time.strftime("%Y-%m-%d %H:%M:%S", utc_time)}')

# 格式化时间
formatted = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print(f'格式化时间: {formatted}')

# 解析时间字符串
time_str = '2024-01-15 14:30:45'
parsed = time.strptime(time_str, '%Y-%m-%d %H:%M:%S')
print(f'解析结果: {parsed}')

# 性能测量
start = time.perf_counter()
# 执行一些操作
time.sleep(1)
end = time.perf_counter()
print(f'耗时: {end - start:.2f} 秒')

# 程序暂停
print('开始...')
time.sleep(2)  # 暂停2秒
print('结束')
```

## 0x04. calendar 模块

```python
import calendar

# 打印日历
print(calendar.month(2024, 1))  # 2024年1月
print(calendar.calendar(2024))  # 2024年全年

# 判断闰年
print(calendar.isleap(2024))  # True
print(calendar.isleap(2023))  # False

# 某月天数
print(calendar.monthrange(2024, 2))  # (3, 29) - 星期三开始，29天
print(calendar.monthrange(2023, 2))  # (2, 28) - 星期三开始，28天

# 某月第一天是星期几
print(calendar.monthcalendar(2024, 1))
# [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], ...]

# 星期几名称
print(calendar.day_name)  # ('Monday', 'Tuesday', ...)
print(calendar.month_name)  # ('', 'January', 'February', ...)
```

## 0x05. 实用工具

### 日期解析器 (dateutil)

```python
# pip install python-dateutil
from dateutil import parser
from datetime import datetime

# 自动解析各种日期格式
date_strings = [
    '2024-01-15',
    '2024/01/15',
    '15 Jan 2024',
    'January 15, 2024',
    '2024-01-15 14:30:45',
    '2024-01-15T14:30:45Z',
]

for date_str in date_strings:
    try:
        dt = parser.parse(date_str)
        print(f'{date_str} -> {dt}')
    except parser.ParserError:
        print(f'{date_str} -> 解析失败')

# 相对时间解析
from dateutil.relativedelta import relativedelta
from datetime import datetime

now = datetime.now()

# 使用 relativedelta
next_month = now + relativedelta(months=1)
last_year = now - relativedelta(years=1)
next_monday = now + relativedelta(weekday=calendar.MONDAY)

print(f'下个月: {next_month}')
print(f'去年: {last_year}')
print(f'下周一: {next_monday}')
```

### 日期范围生成器

```python
from datetime import datetime, timedelta

def date_range(start, end, step=timedelta(days=1)):
    """生成日期范围"""
    current = start
    while current <= end:
        yield current
        current += step

# 使用
start = datetime(2024, 1, 1)
end = datetime(2024, 1, 10)
for dt in date_range(start, end):
    print(dt.strftime('%Y-%m-%d'))

# 工作日生成器
def workday_range(start, end):
    """生成工作日范围"""
    current = start
    while current <= end:
        if current.weekday() < 5:  # 0-4 是周一到周五
            yield current
        current += timedelta(days=1)

# 使用
start = datetime(2024, 1, 1)
end = datetime(2024, 1, 15)
workdays = list(workday_range(start, end))
print(f'工作日数量: {len(workdays)}')
```

### 年龄计算

```python
from datetime import date, datetime

def calculate_age(birthdate):
    """计算年龄"""
    today = date.today()
    age = today.year - birthdate.year
    
    # 检查是否已过生日
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    
    return age

# 使用
birth = date(1990, 5, 15)
age = calculate_age(birth)
print(f'年龄: {age} 岁')

# 更精确的年龄计算
from dateutil.relativedelta import relativedelta

def calculate_age_precise(birthdate):
    """计算精确年龄"""
    today = date.today()
    diff = relativedelta(today, birthdate)
    return f'{diff.years}岁 {diff.months}月 {diff.days}天'

print(calculate_age_precise(birth))
```

### 时间格式化工具

```python
from datetime import datetime, timedelta

def format_relative_time(dt):
    """格式化相对时间（如：3小时前）"""
    now = datetime.now()
    diff = now - dt
    
    if diff.days > 365:
        years = diff.days // 365
        return f'{years}年前'
    elif diff.days > 30:
        months = diff.days // 30
        return f'{months}个月前'
    elif diff.days > 0:
        return f'{diff.days}天前'
    elif diff.seconds > 3600:
        hours = diff.seconds // 3600
        return f'{hours}小时前'
    elif diff.seconds > 60:
        minutes = diff.seconds // 60
        return f'{minutes}分钟前'
    else:
        return '刚刚'

# 使用
past = datetime.now() - timedelta(hours=3, minutes=30)
print(format_relative_time(past))  # 3小时前

past = datetime.now() - timedelta(days=5)
print(format_relative_time(past))  # 5天前
```

### 定时任务调度

```python
import time
from datetime import datetime, timedelta

def schedule_task(task_func, run_time):
    """调度任务在指定时间执行"""
    while True:
        now = datetime.now()
        if now >= run_time:
            task_func()
            break
        time.sleep(1)

def my_task():
    print(f'任务执行于: {datetime.now()}')

# 设置任务在10秒后执行
run_time = datetime.now() + timedelta(seconds=10)
print(f'任务将于 {run_time} 执行')

# 取消注释以运行
# schedule_task(my_task, run_time)
```

## 参考
1. [Python 官方文档 - datetime](https://docs.python.org/3/library/datetime.html)
2. [Python 官方文档 - time](https://docs.python.org/3/library/time.html)
3. [Python 官方文档 - calendar](https://docs.python.org/3/library/calendar.html)
4. [dateutil 文档](https://dateutil.readthedocs.io/)