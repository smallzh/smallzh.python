# 使用Flask搭建Http服务

Python有一些好用的Http框架，能帮我们快速的启动一个Http服务。比较出名的有 Django、Flask等等，Django的功能相对来说，强大很多，适用于复杂一些的Http应用，而Flask则轻量很多，适应于一些简单、小型的Http应用。

对于大型的Web应用，我更倾向于Java来开发，因此，对Django关注并不多。

我更多是在机器学习方面使用Python，用到的Http服务，也只是提供一个api接口，供其他应用调用，所以，算是一个小型、轻量级的Web应用，Flask就更适合一些。

Flask的网址有很多个，相比较来看，这个网址[https://dormousehole.readthedocs.io/en/2.1.2/index.html#api](https://dormousehole.readthedocs.io/en/2.1.2/index.html#api)版本新一些。

这个网站里，从安装到教程，都有，但内容比较多，我当前重在关注快速启动一个Http服务，提供Api接口功能，整理这篇内容。

## 1 安装

```shell
# pip 安装
pip install Flask
# conda 安装
conda install -y Flask
```

## 2 编写启动文件
编写启动脚本，命名为flask_app.py，不要命名为flask.py，会导致启动时报import错误。

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Python World By Flask!"

if __name__ == "__main__":
    app.run()
```

启动命令

```shell
python flask_app.py
```

会报一条警告

```txt
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
```

## 3 访问
浏览器里访问 127.0.0.1:5000

## 4 使用WSGI服务

### 4.1 安装

```shell
# pip安装
pip install gevent
# conda 安装
conda install gevent
```

### 4.2 修改启动文件

修改flask_app.py文件，如下

```python
from flask import Flask
from gevent import pywsgi

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Python World By Flask!"

if __name__ == "__main__":
    # 开发模式下可用
    # app.run()
    # 生产模式下使用
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    server.serve_forever()
```

### 4.3 再次启动并访问

```shell
python flask_app.py
```

不在出现警告信息，并可正常访问

## 修改记录
|版次|时间|修改|
|---|---|---|
|v1|2023.04.28|初步记录flask的安装和启动|