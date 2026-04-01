# 单元测试

单元测试是软件开发中确保代码质量的重要实践。Python 提供了 `unittest` 模块，也有流行的第三方库 `pytest`。

## 0x01. unittest 基本使用

### 编写测试

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

```python
# test_calculator.py
import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
    
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
    
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 100), 0)
    
    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(7, 2), 3.5)
        
        # 测试异常
        with self.assertRaises(ValueError):
            divide(1, 0)

if __name__ == '__main__':
    unittest.main()
```

### 运行测试

```shell
# 运行测试文件
python -m unittest test_calculator.py

# 运行特定测试类
python -m unittest test_calculator.TestCalculator

# 运行特定测试方法
python -m unittest test_calculator.TestCalculator.test_add

# 发现并运行所有测试
python -m unittest discover

# 详细输出
python -m unittest -v test_calculator.py
```

## 0x02. 断言方法

```python
import unittest

class TestAssertions(unittest.TestCase):
    
    def test_equality(self):
        # 相等
        self.assertEqual(1 + 1, 2)
        self.assertNotEqual(1 + 1, 3)
    
    def test_boolean(self):
        # 布尔值
        self.assertTrue(True)
        self.assertFalse(False)
    
    def test_identity(self):
        # 身份
        a = [1, 2, 3]
        b = a
        c = [1, 2, 3]
        self.assertIs(a, b)        # 同一个对象
        self.assertIsNot(a, c)     # 不是同一个对象
        self.assertIsNone(None)
        self.assertIsNotNone(1)
    
    def test_membership(self):
        # 成员关系
        self.assertIn(1, [1, 2, 3])
        self.assertNotIn(4, [1, 2, 3])
    
    def test_comparison(self):
        # 比较
        self.assertGreater(5, 3)
        self.assertGreaterEqual(5, 5)
        self.assertLess(3, 5)
        self.assertLessEqual(5, 5)
    
    def test_type(self):
        # 类型
        self.assertIsInstance(1, int)
        self.assertNotIsInstance(1, float)
    
    def test_regex(self):
        # 正则表达式
        self.assertRegex('hello world', r'hello')
        self.assertNotRegex('hello', r'world')
    
    def test_almost_equal(self):
        # 浮点数近似相等
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=7)
        self.assertNotAlmostEqual(0.1 + 0.2, 0.4)
    
    def test_sequence(self):
        # 序列
        self.assertSequenceEqual([1, 2, 3], [1, 2, 3])
        self.assertListEqual([1, 2, 3], [1, 2, 3])
        self.assertTupleEqual((1, 2), (1, 2))
        self.assertSetEqual({1, 2, 3}, {3, 2, 1})
        self.assertDictEqual({'a': 1}, {'a': 1})
    
    def test_exception(self):
        # 异常
        with self.assertRaises(ValueError):
            int('not a number')
        
        with self.assertRaisesRegex(ValueError, 'invalid literal'):
            int('not a number')
        
        # 检查异常属性
        with self.assertRaises(ValueError) as context:
            int('not a number')
        self.assertIn('invalid literal', str(context.exception))
```

## 0x03. 测试夹具

```python
import unittest
import tempfile
import os

class TestWithFixtures(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """整个测试类开始前执行一次"""
        cls.shared_resource = 'setup once'
        print('setUpClass')
    
    @classmethod
    def tearDownClass(cls):
        """整个测试类结束后执行一次"""
        print('tearDownClass')
    
    def setUp(self):
        """每个测试方法前执行"""
        self.test_data = [1, 2, 3]
        print('setUp')
    
    def tearDown(self):
        """每个测试方法后执行"""
        self.test_data = None
        print('tearDown')
    
    def test_example1(self):
        print('test_example1')
        self.assertEqual(len(self.test_data), 3)
    
    def test_example2(self):
        print('test_example2')
        self.test_data.append(4)
        self.assertEqual(len(self.test_data), 4)

class TestFileOperations(unittest.TestCase):
    
    def setUp(self):
        # 创建临时文件
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        self.temp_file.write('test content')
        self.temp_file.close()
    
    def tearDown(self):
        # 清理临时文件
        os.unlink(self.temp_file.name)
    
    def test_read_file(self):
        with open(self.temp_file.name, 'r') as f:
            content = f.read()
        self.assertEqual(content, 'test content')
```

## 0x04. 跳过测试

```python
import unittest
import sys

class TestSkipping(unittest.TestCase):
    
    @unittest.skip('无条件跳过')
    def test_skip(self):
        self.fail('should not reach here')
    
    @unittest.skipIf(sys.platform == 'win32', 'Windows 上跳过')
    def test_skip_if(self):
        pass
    
    @unittest.skipUnless(sys.platform == 'linux', '仅在 Linux 上运行')
    def test_skip_unless(self):
        pass
    
    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(1, 2)  # 预期失败
    
    def test_skip_dynamically(self):
        if True:  # 某些条件
            self.skipTest('动态跳过')
```

## 0x05. pytest

### 安装和基本使用

```shell
pip install pytest
```

```python
# test_example.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_add_negative():
    assert add(-2, -3) == -5
```

```shell
# 运行测试
pytest test_example.py
pytest test_example.py::test_add
pytest -v test_example.py  # 详细输出
pytest -s test_example.py  # 显示打印
pytest -x test_example.py  # 第一个失败时停止
pytest --lf test_example.py  # 只运行上次失败的测试
pytest --ff test_example.py  # 先运行上次失败的测试
```

### pytest 夹具

```python
import pytest

@pytest.fixture
def sample_data():
    return {'name': 'Alice', 'age': 25}

@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / 'test.txt'
    file.write_text('test content')
    return file

def test_sample_data(sample_data):
    assert sample_data['name'] == 'Alice'
    assert sample_data['age'] == 25

def test_temp_file(temp_file):
    assert temp_file.read_text() == 'test content'

# 夹具作用域
@pytest.fixture(scope='session')
def database_connection():
    # 整个测试会话只创建一次
    conn = create_connection()
    yield conn
    conn.close()

@pytest.fixture(scope='class')
def setup_class():
    # 每个测试类创建一次
    pass

@pytest.fixture(scope='module')
def setup_module():
    # 每个测试模块创建一次
    pass

@pytest.fixture(scope='function')
def setup_function():
    # 每个测试函数创建一次（默认）
    pass
```

### pytest 参数化

```python
import pytest

@pytest.mark.parametrize('a, b, expected', [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    assert a + b == expected

# 多个参数化装饰器
@pytest.mark.parametrize('x', [0, 1])
@pytest.mark.parametrize('y', [2, 3])
def test_multiply(x, y):
    assert x * y == x * y

# 参数化 ID
@pytest.mark.parametrize('input, expected', [
    ('hello', 5),
    ('world', 5),
    pytest.param('', 0, id='empty'),
    pytest.param('a' * 100, 100, id='long'),
])
def test_len(input, expected):
    assert len(input) == expected
```

### pytest 标记

```python
import pytest

@pytest.mark.slow
def test_slow_operation():
    # 标记为慢速测试
    pass

@pytest.mark.skip(reason='尚未实现')
def test_not_implemented():
    pass

@pytest.mark.skipif(sys.platform == 'win32', reason='Windows 不支持')
def test_linux_only():
    pass

@pytest.mark.xfail(reason='已知问题')
def test_known_bug():
    pass

# 自定义标记
@pytest.mark.database
def test_database():
    pass

# 运行特定标记
# pytest -m slow
# pytest -m "not slow"
# pytest -m "database and not slow"
```

## 0x06. Mock

```python
from unittest.mock import Mock, patch, MagicMock

# 创建 Mock 对象
mock = Mock()
mock.method.return_value = 42
assert mock.method() == 42

# 检查调用
mock.method('arg1', 'arg2')
mock.method.assert_called()
mock.method.assert_called_once()
mock.method.assert_called_with('arg1', 'arg2')

# 使用 patch 装饰器
@patch('module.function')
def test_with_mock(mock_function):
    mock_function.return_value = 'mocked'
    result = module.function()
    assert result == 'mocked'

# 使用 patch 上下文管理器
def test_with_context():
    with patch('module.function') as mock_function:
        mock_function.return_value = 'mocked'
        result = module.function()
        assert result == 'mocked'

# Mock 类方法
class MyClass:
    def method(self):
        return 'original'

def test_mock_method():
    obj = MyClass()
    obj.method = Mock(return_value='mocked')
    assert obj.method() == 'mocked'

# MagicMock - 自动创建属性和方法
mock = MagicMock()
mock.attr.method().other.return_value = 42
assert mock.attr.method().other() == 42
```

### 实际应用

```python
import requests
from unittest.mock import patch, Mock

def fetch_user(user_id):
    response = requests.get(f'https://api.example.com/users/{user_id}')
    return response.json()

@patch('requests.get')
def test_fetch_user(mock_get):
    # 设置 mock 返回值
    mock_response = Mock()
    mock_response.json.return_value = {'id': 1, 'name': 'Alice'}
    mock_get.return_value = mock_response
    
    # 调用被测试函数
    user = fetch_user(1)
    
    # 验证结果
    assert user['name'] == 'Alice'
    
    # 验证调用
    mock_get.assert_called_once_with('https://api.example.com/users/1')
```

## 0x07. 测试最佳实践

### 测试目录结构

```
project/
├── src/
│   ├── __init__.py
│   ├── calculator.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   └── test_utils.py
└── pyproject.toml
```

### pytest 配置

```toml
# pyproject.toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --tb=short"
markers = [
    "slow: marks tests as slow",
    "database: marks tests that need database",
]
```

### 测试原则

```python
"""
1. 测试应该是独立的
2. 测试应该是可重复的
3. 测试应该是快速的
4. 测试应该有清晰的命名
5. 每个测试只测试一件事
6. 使用夹具减少重复
7. 测试边界条件和异常情况
"""

# 好的测试命名
def test_user_creation_with_valid_data():
    pass

def test_user_creation_with_invalid_email_raises_error():
    pass

def test_user_age_must_be_positive():
    pass

# 好的测试结构 (AAA 模式)
def test_example():
    # Arrange - 准备测试数据
    data = [1, 2, 3]
    
    # Act - 执行被测试操作
    result = sum(data)
    
    # Assert - 验证结果
    assert result == 6
```

## 参考
1. [Python 官方文档 - unittest](https://docs.python.org/3/library/unittest.html)
2. [pytest 官方文档](https://docs.pytest.org/)
3. [unittest.mock 文档](https://docs.python.org/3/library/unittest.mock.html)