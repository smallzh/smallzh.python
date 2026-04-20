"""测试：Python datetime相关知识点的 pytest 风格单元测试
覆盖日期/时间、时区、格式化以及基础时间工具函数的用法。
使用纯标准库实现，测试用例自包含，不依赖外部依赖。
"""

from datetime import date, time, datetime, timedelta, timezone
try:
    from zoneinfo import ZoneInfo
    from zoneinfo._common import ZoneInfoNotFoundError
except (ImportError, ModuleNotFoundError):
    ZoneInfo = None
    ZoneInfoNotFoundError = Exception
import time as _time
import calendar


def test_date_basic():
    """TestDate：date 类型基本属性与方法"""
    d = date.today()
    assert isinstance(d, date)
    # year/month/day 属性
    assert hasattr(d, "year") and hasattr(d, "month") and hasattr(d, "day")
    assert 1 <= d.year


def test_time_basic():
    """TestTime：time 类型基本属性"""
    t = time(14, 30, 45)
    assert t.hour == 14
    assert t.minute == 30
    assert t.second == 45


def test_datetime_basic():
    """TestDatetime：datetime 的创建与属性"""
    now = datetime.now()
    assert isinstance(now, datetime)
    specific = datetime(2020, 1, 2, 3, 4, 5)
    assert specific.year == 2020
    assert specific.month == 1
    assert specific.day == 2
    assert specific.hour == 3
    assert specific.minute == 4
    assert specific.second == 5


def test_timedelta_and_date_arithmetic():
    """TestTimedelta：时间差与日期运算，以及 replace()"""
    dt = datetime(2020, 1, 1, 12, 0, 0)
    delta = timedelta(days=1, hours=2)
    new_dt = dt + delta
    assert new_dt == datetime(2020, 1, 2, 14, 0, 0)

    d1 = datetime(2020, 1, 3)
    d0 = datetime(2020, 1, 1)
    diff = d1 - d0
    assert diff.days == 2
    assert d0 < d1
    assert d0 == datetime(2020, 1, 1)

    replaced = dt.replace(year=2021)
    assert replaced.year == 2021
    assert replaced.month == dt.month


def test_strftime_strptime_and_timezone():
    """TestStrftimeStrptime 与 TestTimezone：格式化/解析和时区转换"""
    dt = datetime(2023, 4, 5, 6, 7, 8)
    s = dt.strftime("%Y-%m-%d %H:%M:%S")
    assert s == "2023-04-05 06:07:08"
    parsed = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
    assert parsed == dt

    # 时区相关：如果系统有tzdata则测试，否则跳过
    try:
        dt_utc = datetime(2020, 1, 1, 12, 0, 0, tzinfo=ZoneInfo("UTC"))
        dt_sh = dt_utc.astimezone(ZoneInfo("Asia/Shanghai"))
        assert dt_sh.tzinfo is not None
        assert dt_sh.utcoffset().total_seconds() == 8 * 3600
    except ZoneInfoNotFoundError:
        pass  # Windows上可能没有tzdata，跳过时区测试


def test_time_module_basic():
    """TestTimeModule：time 模块的基础用法"""
    import time

    ts = time.time()
    assert isinstance(ts, float)
    t_before = time.time()
    time.sleep(0.001)
    t_after = time.time()
    assert t_after >= t_before

    # 格式化与解析（UTC 时间基于 GMT/UTC，结果稳定）
    s = time.strftime("%H:%M:%S", time.gmtime(0))
    assert s == "00:00:00"
    st = time.strptime("1970-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
    assert st.tm_year == 1970 and st.tm_mon == 1 and st.tm_mday == 1

    t0 = time.perf_counter()
    time.sleep(0.0001)
    t1 = time.perf_counter()
    assert t1 >= t0


def test_calendar_basic_and_date_range_and_age():
    """TestCalendar：日历相关、date_range 与年龄计算示例"""
    # 日历功能
    assert calendar.isleap(2020) is True
    assert calendar.isleap(1900) is False
    assert calendar.monthrange(2020, 2)[1] == 29
    assert len(list(calendar.day_name)) >= 7
    assert calendar.month_name[1] == "January"

    # 日期范围生成器示例（自包含起点，不包含终点）
    def date_range(start: date, end: date, step: timedelta = timedelta(days=1)):
        cur = start
        while cur < end:
            yield cur
            cur = cur + step
    rng = list(date_range(date(2020, 1, 1), date(2020, 1, 4)))
    assert rng == [date(2020, 1, 1), date(2020, 1, 2), date(2020, 1, 3)]

    # 工作日范围（周一至周五）示例
    def workday_range(start: date, end: date):
        cur = start
        while cur < end:
            if cur.weekday() < 5:
                yield cur
            cur = cur + timedelta(days=1)
    workdays = list(workday_range(date(2020, 1, 4), date(2020, 1, 8)))  # 2020-01-04 周六开始，结束于 2020-01-08 周三
    assert workdays == [date(2020, 1, 6), date(2020, 1, 7)]  # 仅周一、周二、周三之间的工作日

    # 年龄计算
    def calculate_age(birth_date: date, today: date | None = None) -> int:
        if today is None:
            today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
    assert calculate_age(date(2000, 1, 1), today=date(2020, 1, 1)) == 20
