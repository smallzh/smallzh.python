"""测试：Python 正则表达式（re 模块）核心用法，覆盖常见模式与常用应用"""
import re


def test_search_basic():
    """TestSearch：re.search 基本匹配与 Match 对象属性"""
    s = "abc 123 def 456"
    m = re.search(r"\d+", s)
    assert m is not None
    assert m.group() == "123"
    assert m.span() == (4, 7)
    assert m.start() == 4
    assert m.end() == 7


def test_match_basic():
    """TestMatch：re.match 与 ^ 匹配起始位置的差异"""
    m = re.match(r"Hello", "Hello world")
    assert m is not None and m.group() == "Hello"
    m_none = re.match(r"Hello", "Hi Hello")
    assert m_none is None


def test_findall_and_groups():
    s = "a1 b22 c333"
    res = re.findall(r"\d+", s)
    assert res == ["1", "22", "333"]
    # 带分组findall返回元组列表，只有连续两位数字才匹配
    res_groups = re.findall(r"(\d)(\d)", "12 34 56")
    assert res_groups == [("1", "2"), ("3", "4"), ("5", "6")]


def test_finditer_and_sub():
    s = "foo 123 foo 456"
    it = re.finditer(r"\d+", s)
    nums = [m.group() for m in it]
    assert nums == ["123", "456"]
    s2 = re.sub(r"foo", "bar", s)
    assert s2 == "bar 123 bar 456"
    s3 = re.sub(r"foo", "bar", s, count=1)
    assert s3 == "bar 123 foo 456"


def test_split_and_split_with_groups():
    s = "a,b;c"
    assert re.split(r"[,;]", s) == ["a", "b", "c"]
    assert re.split(r"([,;])", s) == ["a", ",", "b", ";", "c"]
    assert re.split(r"[,;]", s, maxsplit=1) == ["a", "b;c"]


def test_metacharacters_and_character_classes():
    # . 匹配任意字符（除换行）
    assert re.match(r".", ".").group() == "."
    # ^、$ 多行/边界
    s = "start\nend"
    assert re.search(r"^start", s, flags=re.M) is not None

    # 字符类
    assert re.match(r"[abc]", "a").group() == "a"
    assert re.match(r"[^abc]", "d").group() == "d"
    assert re.match(r"[a-z]", "q").group() == "q"
    assert re.match(r"[0-9]", "7").group() == "7"
    # 预定义字符类
    assert re.match(r"\d", "9").group() == "9"
    assert re.match(r"\D", "x").group() == "x"
    assert re.match(r"\w", "_").group() == "_"
    assert re.match(r"\W", "!").group() == "!"
    assert re.search(r"\s", " ") is not None


def test_quantifiers():
    # 具体次数
    assert re.match(r"a{2,3}", "aaa").group() == "aaa"
    # 贪婪 vs 非贪婪
    assert re.findall(r"a+", "aaaa") == ["aaaa"]
    assert re.findall(r"a+?", "aaaa") == ["a", "a", "a", "a"]


def test_groups_and_lookaround():
    m = re.match(r"(cat|dog) (\d+)", "cat 123")
    assert m.group(1) == "cat" and m.group(2) == "123"
    assert m.groupdict() == {}
    # 命名分组与反向引用
    m2 = re.match(r"(?P<name>\w+)-(\d+)", "item-42")
    assert m2.group("name") == "item"
    # 前瞻/后顾
    m3 = re.search(r"(?<=cat )\d+", "cat 999")
    assert m3 is not None and m3.group() == "999"


def test_compile_and_flags():
    p = re.compile(r"abc", re.IGNORECASE | re.MULTILINE | re.DOTALL)
    assert p.search("ABC") is not None


def test_practical_applications():
    # 验证邮箱格式（+号需要包含在字符类中）
    email = "user.name+tag@example.co.uk"
    assert re.match(r"^[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}$", email)
    # 验证手机号（简化：中国内地手机号以 1 开头，共 11 位）
    assert re.match(r"^1\d{10}$", "13800138000")
    # 验证 IP 地址（简单范围检查）
    ip = "192.168.0.1"
    parts = ip.split(".")
    valid_ip = len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)
    assert valid_ip
    # 提取邮箱
    text = "Contact: alice@example.com, bob@mail.co"
    emails = re.findall(r"[\w\.-]+@[\w\.-]+\.[A-Za-z]+", text)
    assert emails == ["alice@example.com", "bob@mail.co"]
    # 简单脱敏处理
    e = "user@example.com"
    local, _, domain = e.partition("@")
    masked = local[0] + "***" + "@" + domain
    assert masked.startswith("u***@")
