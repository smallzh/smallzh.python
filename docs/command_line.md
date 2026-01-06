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