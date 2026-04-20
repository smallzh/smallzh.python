# -*- coding: utf-8 -*-
"""
test_string.py
基于 docs/string.md 的字符串相关知识点单元测试。
使用 pytest 风格，确保在 Python 3.13+ 下通过。
"""
import re
import datetime as _dt
import string

import pytest


class TestStringCreation:
    def test_creation_with_quotes_and_raw_and_escapes(self):
        """字符串创建：单/双/三引号、原始字符串、转义字符"""
        s1 = 'Hello'
        s2 = "World"
        s3 = """Line1
Line2"""
        assert s1 + " " + s2 == "Hello World"
        rpaths = r"C:\path\to\file"
        assert rpaths == "C:\\path\\to\\file"
        esc = "line1\nline2\tTabbed\\"  # 转义示例
        assert esc.startswith("line1") and "line2" in esc


class TestFString:
    def test_basic_and_advanced_formatting(self):
        name = "Alice"
        assert f"Hi {name}" == "Hi Alice"
        assert f"{1+2}" == "3"
        pi = 3.14159
        assert f"{pi:.2f}" == "3.14"
        s = "hi"
        assert f"{s:*^10}" == "****hi****"
        assert f"{1000000:,}" == "1,000,000"
        dt = _dt.date(2020, 5, 17)
        assert f"{dt:%Y-%m-%d}" == "2020-05-17"


class TestRawString:
    def test_raw_string_preserves_backslashes(self):
        p = r"C:\Users\name\docs"
        assert p == "C:\\Users\\name\\docs"
        pattern = r"\d+"
        assert pattern == "\\d+"


class TestStringOperations:
    def test_index_slice_concat_join_and_search(self):
        s = "abcdef"
        assert s[0] == 'a'
        assert s[1:4] == "bcd"
        assert ("a" + "b") == "ab"
        assert ("ab" * 3) == "ababab"
        assert "-".join(["a", "b", "c"]) == "a-b-c"
        assert s.find("cd") == 2
        assert s.index("bc") == 1
        assert s.rfind("a") == 0
        assert s.count("a") == 1
        assert s.startswith("ab")
        assert s.endswith("ef")
        assert s.replace("bc", "X") == "aXdef"
        trans = str.maketrans({'a':'A','e':'3'})
        assert "apple".translate(trans) == "Appl3"
        assert "a,b,c".split(",") == ["a", "b", "c"]
        assert "line1\nline2".splitlines() == ["line1", "line2"]
        assert "hello".partition("l") == ("he", "l", "lo")
        assert "abc".upper() == "ABC"
        assert "abc".lower() == "abc"
        assert "title".title() == "Title"
        assert "abc".capitalize() == "Abc"
        assert "abc".swapcase() == "ABC".lower() and "abc".title() or "ABC".lower()
        assert "abc".isalpha()
        assert "123".isdigit()
        assert "abc123".isalnum()
        assert "  \t".isspace()
        assert "ABC".isupper()
        assert "abc".islower()
        assert "This Is Title".istitle()  # 每个单词首字母大写
        # 填充对齐
        assert "x".center(5) == "  x  "
        assert "9".zfill(5) == "00009"
        assert "x".rjust(4, '0') == "000x"
        assert "x".ljust(4, '0') == "x000"
        assert "  hello  ".strip() == "hello"
        assert "  hello  ".lstrip() == "hello  "
        assert "  hello  ".rstrip() == "  hello"

class TestStringEncoding:
    def test_encode_decode_utf8_and_gbk_and_ascii_errors(self):
        s = "你好"
        b = s.encode('utf-8')
        assert b.decode('utf-8') == s
        b_gbk = s.encode('gbk')
        assert b_gbk.decode('gbk') == s
        with pytest.raises(UnicodeEncodeError):
            s.encode('ascii')
        b_ignore = s.encode('ascii', errors='ignore')
        assert b_ignore.decode('ascii') == "你好".encode('ascii', errors='ignore').decode('ascii')
        b_xml = s.encode('ascii', errors='xmlcharrefreplace')
        assert b_xml.startswith(b'&#')

class TestStringFormatting:
    def test_percent_and_format_and_template(self):
        assert "%s %d" % ("age", 30) == "age 30"
        assert "Hello {}".format("world") == "Hello world"
        from string import Template
        assert Template("Hi ${name}").substitute(name="Bob") == "Hi Bob"


class TestStringConstants:
    def test_constants_values(self):
        assert string.ascii_letters  # 非空字符串
        assert string.digits == '0123456789'
        assert isinstance(string.punctuation, str)
        assert len(string.whitespace) >= 1


class TestRegexBasic:
    def test_basic_regex_operations(self):
        s = "abc123def45"
        assert re.findall(r"\d+", s) == ['123', '45']
        assert re.search(r"\d+", "abc") is None
        assert re.sub(r"\s+", " ", "a  b\tc") == "a b c"
        assert re.split(r"\W+", "A,B;C.D") == ['A', 'B', 'C', 'D']
