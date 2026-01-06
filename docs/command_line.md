# 读取命令行参数

## 1 argparse包

Python中使用 argparse 包处理 命令行参数，如下，假定文件名为： arg_example.py 

```python
# import the necessary packages
import argparse
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True,
	help="name of the user")
args = vars(ap.parse_args())
# display a friendly message to the user
print("Hi there {}, it's nice to meet you!".format(args["name"]))
```

## 2 vars函数

将命令行参数，转换成字段

argparse模块是Python自带的一个模块，能够解析`sys.argv`的值，而且能自动生成help和其他的一些参数信息。官网URL：[https://docs.python.org/3/library/argparse.html](https://docs.python.org/3/library/argparse.html)

## 0x01.核心类
argparse的核心是`argparse.argparse.ArgumentParser`这个类，通过创建他的一个实例对象来使用：

```python
parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
```

常用的几个参数

|参数|说明|
|---|---|
|prog|程序的名称|
|usage|使用说明|
|description|程序的一个描述说明|
|epilog|最终的结束语|

参考：[官网地址](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser)

## 0x02.核心方法 

### 1. add_argument
全名：ArgumentParser.add_argument()，用于添加命令行参数

|参数|说明|
|---|---|
|name or flags|参数的名称，比如 `'foo'` 或 `'-f', '--foo'`

参考: [官网地址](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument)

### 2.  add_group
全名：ArgumentParser.add_group()，添加命令行分组

|参数|说明|
|---|---|

### 3. parse_args
全名：ArgumentParser.parse_args()，解析sys.argv的值

|参数|说明|
|---|---|

## 0x03. Demo
```python
parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')



```

## 0xFF.关键概念
1. sys.argv：命令行参数
2. argparse.ArgumentParser：解析类
