# 使用setuptool工具


setuptool是Python项目的构建工具，官网：[https://setuptools.pypa.io/en/latest/](https://setuptools.pypa.io/en/latest/)，github网址：[https://github.com/pypa/setuptools](https://github.com/pypa/setuptools)


配合build使用，build 官网：[https://build.pypa.io/en/latest/](https://build.pypa.io/en/latest/)

通过`setup.py`配置文件对其进行配置。

它扩展了标准库`distutils`，提供了元数据管理、依赖管理、源代码打包、开发模式、命名空间包支持及定义入口点等多种功能。

## 0x01. 安装
```shell
pip install setuptools
# 或者
pip install --upgrade setuptools[core]
```

## 0x02. setup.py文件

打包Python项目的构建工具，配置文件相关内容，整理如下：

```python
from setuptools import setup

setup(
    name='myproject',
    version='0.1',
    description='A simple Python project',
    author='Your Name',
    author_email='your@email.com',
    packages=['myproject'],
    install_requires=[
        'dependency1',
        'dependency2',
    ],
)
```

## 0x03.setuptool的构建命令
```shell
#在项目目录中创建一个包含了源代码包的 dist 目录
python setup.py sdist
# 创建一个Python 的二进制包格式 .whl 文件
python setup.py bdist_wheel
# 发布到 Python的 PyPi 中
python setup.py sdist bdist_wheel
twine upload dist/*
```

## 0x02. 配合build
```shell
# 再或者 使用 build
pip install --upgrade build
# 如果使用 build，需要 pyproject.toml 文件
python -m build
```

文件`pyproject.toml` 内容：
```txt
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
```

## 关键概念
1. distutils
2. 元数据管理
3. dependency management（依赖管理）：
4. entry points（入口点）：
5. 源代码打包
6. package discovery（包扫描）：
7. namespace packages（命名空间包）：
8. Egg格式
9. Wheel格式
10. Data Files（数据文件）：
11. Development mode（开发模式）：
12. PyPi（Python包仓库）：