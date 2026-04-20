"""异常处理核心知识点测试 - 基于 docs/exception.md"""

import time
from contextlib import suppress
from dataclasses import dataclass
from typing import Optional, Tuple, Any


# ============================================================
# 0x01. 常见异常类型
# ============================================================

class TestCommonExceptions:
    """常见异常类型测试"""

    def test_name_error(self):
        """NameError - 变量名未定义"""
        try:
            _ = undefined_variable
            assert False, "Should have raised NameError"
        except NameError:
            pass

    def test_value_error(self):
        """ValueError - 值错误"""
        try:
            int('abc')
            assert False, "Should have raised ValueError"
        except ValueError:
            pass

    def test_index_error(self):
        """IndexError - 索引越界"""
        try:
            _ = [1, 2, 3][10]
            assert False, "Should have raised IndexError"
        except IndexError:
            pass

    def test_key_error(self):
        """KeyError - 字典键不存在"""
        try:
            _ = {'a': 1}['b']
            assert False, "Should have raised KeyError"
        except KeyError:
            pass

    def test_type_error(self):
        """TypeError - 类型错误"""
        try:
            _ = 'hello' + 5
            assert False, "Should have raised TypeError"
        except TypeError:
            pass

    def test_zero_division_error(self):
        """ZeroDivisionError - 除零错误"""
        try:
            _ = 10 / 0
            assert False, "Should have raised ZeroDivisionError"
        except ZeroDivisionError:
            pass

    def test_file_not_found_error(self):
        """FileNotFoundError - 文件不存在"""
        try:
            open('nonexistent_file_12345.txt', 'r')
            assert False, "Should have raised FileNotFoundError"
        except FileNotFoundError:
            pass


# ============================================================
# 0x02. 基本异常处理
# ============================================================

class TestTryExcept:
    """try-except基本测试"""

    def test_catch_exception(self):
        """捕获异常"""
        try:
            result = 10 / 0
        except ZeroDivisionError:
            result = 'caught'
        assert result == 'caught'

    def test_catch_as_object(self):
        """捕获异常对象"""
        try:
            result = 10 / 0
        except ZeroDivisionError as e:
            assert type(e).__name__ == 'ZeroDivisionError'
            assert 'division' in str(e).lower() or 'zero' in str(e).lower()

    def test_catch_multiple_exceptions(self):
        """捕获多种异常"""
        caught = None
        try:
            int('abc')
        except ValueError:
            caught = 'ValueError'
        except ZeroDivisionError:
            caught = 'ZeroDivisionError'
        assert caught == 'ValueError'

    def test_catch_combined(self):
        """合并捕获多种异常"""
        caught = False
        try:
            int('abc')
        except (ValueError, ZeroDivisionError) as e:
            caught = True
        assert caught is True


class TestTryExceptElse:
    """try-except-else测试"""

    def test_else_no_exception(self):
        """else块在没有异常时执行"""
        else_executed = False
        try:
            number = int('42')
        except ValueError:
            pass
        else:
            else_executed = True
        assert else_executed is True

    def test_else_with_exception(self):
        """else块在有异常时不执行"""
        else_executed = False
        try:
            int('abc')
        except ValueError:
            pass
        else:
            else_executed = True
        assert else_executed is False


class TestTryFinally:
    """try-finally测试"""

    def test_finally_always_executes(self):
        """finally总是执行"""
        finally_executed = False
        try:
            x = 10 / 2
        finally:
            finally_executed = True
        assert finally_executed is True

    def test_finally_after_exception(self):
        """finally在异常后也执行"""
        finally_executed = False
        try:
            _ = 10 / 0
        except ZeroDivisionError:
            pass
        finally:
            finally_executed = True
        assert finally_executed is True

    def test_full_structure(self):
        """完整 try-except-else-finally"""
        finally_executed = False
        else_executed = False
        try:
            result = 10 / 2
        except ZeroDivisionError:
            pass
        else:
            else_executed = True
        finally:
            finally_executed = True
        assert else_executed is True
        assert finally_executed is True


# ============================================================
# 0x03. 主动抛出异常
# ============================================================

class TestRaise:
    """raise语句测试"""

    def test_raise_value_error(self):
        """raise ValueError"""
        def set_age(age):
            if age < 0:
                raise ValueError('年龄不能为负数')
            return age

        try:
            set_age(-5)
            assert False, "Should have raised ValueError"
        except ValueError as e:
            assert '负数' in str(e)

    def test_raise_with_message(self):
        """raise带消息"""
        def divide(a, b):
            if b == 0:
                raise ZeroDivisionError(f'不能将 {a} 除以零')
            return a / b

        try:
            divide(10, 0)
        except ZeroDivisionError as e:
            assert '10' in str(e)

    def test_reraise(self):
        """重新raise当前异常"""
        def process_data(data):
            try:
                result = int(data)
            except ValueError:
                raise

        try:
            process_data('abc')
            assert False, "Should have raised ValueError"
        except ValueError:
            pass


# ============================================================
# 自定义异常
# ============================================================

class TestCustomException:
    """自定义异常测试"""

    def test_custom_exception_basic(self):
        """基本自定义异常"""
        class CustomError(Exception):
            pass

        try:
            raise CustomError('自定义错误')
        except CustomError as e:
            assert str(e) == '自定义错误'

    def test_custom_exception_with_attributes(self):
        """自定义异常带属性"""
        class ValidationError(Exception):
            def __init__(self, field, message):
                self.field = field
                self.message = message
                super().__init__(f'{field}: {message}')

        try:
            raise ValidationError('age', '必须是整数')
        except ValidationError as e:
            assert e.field == 'age'
            assert e.message == '必须是整数'
            assert 'age' in str(e)

    def test_custom_exception_hierarchy(self):
        """自定义异常层级"""
        class CustomError(Exception):
            pass

        class BusinessError(CustomError):
            def __init__(self, code, message):
                self.code = code
                self.message = message
                super().__init__(f'[{code}] {message}')

        try:
            raise BusinessError('ORDER_001', '订单金额必须大于0')
        except BusinessError as e:
            assert e.code == 'ORDER_001'
        except CustomError:
            assert False, "Should have caught as BusinessError"

    def test_catch_parent_catches_child(self):
        """父异常类能捕获子异常"""
        class CustomError(Exception):
            pass

        class ValidationError(CustomError):
            pass

        caught_as_parent = False
        try:
            raise ValidationError('test')
        except CustomError:
            caught_as_parent = True
        assert caught_as_parent is True


# ============================================================
# 0x04. 异常链
# ============================================================

class TestExceptionChain:
    """异常链测试"""

    def test_raise_from(self):
        """raise ... from e 保留原始异常"""
        def connect_database():
            try:
                raise ConnectionError('数据库连接失败')
            except ConnectionError as e:
                raise RuntimeError('无法初始化应用') from e

        try:
            connect_database()
        except RuntimeError as e:
            assert str(e) == '无法初始化应用'
            assert isinstance(e.__cause__, ConnectionError)

    def test_raise_from_none(self):
        """raise ... from None 隐藏原始异常"""
        def safe_operation():
            try:
                result = 1 / 0
            except ZeroDivisionError:
                raise ValueError('计算错误') from None

        try:
            safe_operation()
        except ValueError as e:
            assert str(e) == '计算错误'
            assert e.__cause__ is None


# ============================================================
# 0x05. 异常最佳实践
# ============================================================

class TestExceptionBestPractice:
    """异常最佳实践测试"""

    def test_dict_get_vs_try_except(self):
        """使用dict.get()而非try/except KeyError"""
        d = {'a': 1}

        # 好的做法
        value = d.get('b', 'not found')
        assert value == 'not found'

    def test_suppress_context(self):
        """contextlib.suppress抑制特定异常"""
        with suppress(FileNotFoundError):
            open('nonexistent_file_12345.txt', 'r')
        # 没有抛出异常，测试通过

    def test_suppress_only_matching(self):
        """suppress只抑制匹配的异常"""
        with suppress(ZeroDivisionError):
            _ = 1 / 0
        # ZeroDivisionError被抑制

        caught = False
        try:
            with suppress(ZeroDivisionError):
                int('abc')
        except ValueError:
            caught = True
        assert caught is True


# ============================================================
# 重试机制
# ============================================================

class TestRetryPattern:
    """重试机制测试"""

    def test_retry_decorator(self):
        """简单重试装饰器"""
        call_count = 0

        def retry(func=None, *, max_attempts=3):
            if func is None:
                return lambda f: retry(f, max_attempts=max_attempts)
            def wrapper(*args, **kwargs):
                last_exception = None
                for attempt in range(max_attempts):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        last_exception = e
                raise last_exception
            return wrapper

        @retry(max_attempts=3)
        def flaky_func():
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise ValueError('not yet')
            return 'success'

        result = flaky_func()
        assert result == 'success'
        assert call_count == 3

    def test_retry_exhausted(self):
        """重试次数耗尽"""
        def retry(func=None, *, max_attempts=3):
            if func is None:
                return lambda f: retry(f, max_attempts=max_attempts)
            def wrapper(*args, **kwargs):
                last_exception = None
                for attempt in range(max_attempts):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        last_exception = e
                raise last_exception
            return wrapper

        @retry(max_attempts=3)
        def always_fail():
            raise ValueError('always fails')

        try:
            always_fail()
            assert False, "Should have raised ValueError"
        except ValueError as e:
            assert 'always fails' in str(e)


# ============================================================
# 安全操作模式
# ============================================================

class TestSafeOperation:
    """安全操作模式测试"""

    def test_result_tuple_pattern(self):
        """返回(结果, 错误)元组"""
        def safe_divide(a: float, b: float) -> Tuple[Optional[float], Optional[str]]:
            try:
                return a / b, None
            except ZeroDivisionError:
                return None, '除数不能为零'

        result, error = safe_divide(10, 2)
        assert result == 5.0
        assert error is None

        result, error = safe_divide(10, 0)
        assert result is None
        assert error == '除数不能为零'

    def test_result_dataclass_pattern(self):
        """Result dataclass模式"""
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

        r1 = safe_operation('42')
        assert r1.success is True
        assert r1.data == 42

        r2 = safe_operation('abc')
        assert r2.success is False
        assert r2.error is not None

    def test_exception_collection(self):
        """异常收集模式"""
        def process_item(item):
            if item < 0:
                raise ValueError(f'负数不允许: {item}')
            return item ** 2

        def process_batch(items):
            errors = []
            results = []
            for item in items:
                try:
                    results.append(process_item(item))
                except Exception as e:
                    errors.append({
                        'item': item,
                        'error': str(e),
                        'type': type(e).__name__
                    })
            return results, errors

        results, errors = process_batch([1, -2, 3, -4, 5])
        assert results == [1, 9, 25]
        assert len(errors) == 2
        assert errors[0]['type'] == 'ValueError'
