#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""测试 json 标准库的编码/解码及自定义编码器/解码器等特性"""

import json
import datetime
from decimal import Decimal


def test_json_basic_roundtrip():
    data = {
        'a': 1,
        'b': [1, 2, 3],
        'c': '中文'
    }
    s = json.dumps(data)
    data2 = json.loads(s)
    assert data2 == data


def test_json_file_operations(tmp_path):
    data = {'note': '测试', 'value': 42}
    p = tmp_path / 'data.json'
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
    with open(p, 'r', encoding='utf-8') as f:
        data2 = json.load(f)
    assert data2 == data


def test_json_formatting_options():
    data = {'b': 2, 'a': 1}
    s_indent = json.dumps(data, indent=2, sort_keys=True)
    s_separators = json.dumps(data, separators=(',', ':'))
    s_sort = json.dumps(data, sort_keys=True)
    assert s_indent.startswith('{\n  "a"')  # indentation 2 spaces, key order sorted
    assert '"a"' in s_sort and '"b"' in s_sort
    assert isinstance(s_separators, str)


def test_custom_encoder_datetime_decimal_and_set():
    class DateTimeEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime.datetime):
                return obj.isoformat()
            if isinstance(obj, Decimal):
                return float(obj)
            if isinstance(obj, set):
                return list(obj)
            return super().default(obj)

    dt = datetime.datetime(2020, 1, 2, 3, 4, 5)
    data = {'t': dt, 'd': Decimal('12.34'), 's': {1, 2}}
    s = json.dumps(data, cls=DateTimeEncoder)
    assert dt.isoformat() in s
    assert '12.34' in s or '12.34' in s


def test_custom_decoder_object_hook():
    class Person:
        def __init__(self, name):
            self.name = name

    def object_hook(d):
        if d.get('__type__') == 'Person':
            return Person(d['name'])
        return d

    payload = {'__type__': 'Person', 'name': 'Alice'}
    s = json.dumps(payload)
    obj = json.loads(s, object_hook=object_hook)
    assert isinstance(obj, Person) and obj.name == 'Alice'


def test_json_utils_equality_with_sort_and_roundtrip():
    a = {'x': 1, 'y': 2}
    b = {'y': 2, 'x': 1}
    assert json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)
