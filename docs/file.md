# 如何处理文件？

使用内部函数`open()`来读取一个文件，open函数会返回一个`fileObject`对象。
通常的写法是

```python
# 以文本模式打开文件
with open('file', encoding='utf-8') as f:
    read_data = f.read()

# 以二进制模式 打开文件
with open('file', 'rb') as f:
    bi_data = f.read()
```

如果不使用`with`，需要手动调`f.close()` 进行关闭。

在文本模式下的读取和写入，会自动替换平台相关的换行符(Unix为`\n`，Window为`\r\n`)，注意对图片、可执行程序的影响，这类文件通常以二进制方式读取。

文件对象的常用方法：

|名称|含义|
|---|---|
|read|读取全部数据|
|readline|逐行读取文本内容|
|readlines|读取文件的所有行|
|write|将内容写入到文件中|

## os.path
常用的路径操作，对于目录和文件，我们常用的操作就是 获取父级目录、获取文件名称、获取绝对路径等等

|名称|含义|
|---|---|
|os.path.abspath|获取一个路径的绝对路径|
|os.path.basename|获取路径的最后一个名称，通常用来获取文件名|
|os.path.dirname|获取一个路径的父级名称|
|os.path.isdir|判断是否为一个目录|
|os.path.isfile|判断是否为一个文件|
|os.path.exists|判断一个文件是否存在|


## pathlib

更全面的路径操作，使用pathlib 库来完成

查看文件编码

```python
import chardet
data = open('file_path', 'rb').read()
encode = chardet.detect(data)
print(encode)
```