# HTTP 请求库

`requests` 是 Python 中最流行的 HTTP 请求库，简洁易用。

## 0x01. 安装

```shell
pip install requests
```

## 0x02. 基本请求

### GET 请求

```python
import requests

# 基本 GET 请求
response = requests.get('https://httpbin.org/get')
print(response.status_code)  # 200
print(response.text)         # 响应文本
print(response.json())       # JSON 响应

# 带参数的 GET 请求
params = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://httpbin.org/get', params=params)
print(response.url)  # 完整 URL

# 带请求头
headers = {'User-Agent': 'MyApp/1.0'}
response = requests.get('https://httpbin.org/get', headers=headers)
```

### POST 请求

```python
import requests

# 发送表单数据
data = {'username': 'user', 'password': 'pass'}
response = requests.post('https://httpbin.org/post', data=data)

# 发送 JSON 数据
json_data = {'name': 'Alice', 'age': 25}
response = requests.post('https://httpbin.org/post', json=json_data)

# 发送文件
files = {'file': open('report.csv', 'rb')}
response = requests.post('https://httpbin.org/post', files=files)
```

### 其他请求方法

```python
import requests

# PUT 请求
response = requests.put('https://httpbin.org/put', data={'key': 'value'})

# DELETE 请求
response = requests.delete('https://httpbin.org/delete')

# HEAD 请求
response = requests.head('https://httpbin.org/get')

# OPTIONS 请求
response = requests.options('https://httpbin.org/get')

# PATCH 请求
response = requests.patch('https://httpbin.org/patch', data={'key': 'value'})
```

## 0x03. 响应处理

### 响应属性

```python
import requests

response = requests.get('https://httpbin.org/get')

# 状态码
print(response.status_code)  # 200
print(response.ok)           # True (200-299)
print(response.reason)       # OK

# 响应头
print(response.headers)
print(response.headers['Content-Type'])

# 响应内容
print(response.text)         # 文本内容
print(response.content)      # 二进制内容
print(response.json())       # JSON 内容

# 编码
print(response.encoding)     # UTF-8
response.encoding = 'utf-8'

# URL
print(response.url)          # 请求的 URL
print(response.history)      # 重定向历史

# Cookies
print(response.cookies)
```

### 异常处理

```python
import requests
from requests.exceptions import (
    HTTPError,
    ConnectionError,
    Timeout,
    RequestException
)

try:
    response = requests.get('https://httpbin.org/status/404')
    response.raise_for_status()  # 抛出 HTTPError
except HTTPError as e:
    print(f'HTTP 错误: {e}')
except ConnectionError:
    print('连接错误')
except Timeout:
    print('请求超时')
except RequestException as e:
    print(f'请求错误: {e}')
```

## 0x04. 高级功能

### 会话

```python
import requests

# 使用会话保持连接和 cookies
session = requests.Session()

# 设置会话级别的参数
session.headers.update({'User-Agent': 'MyApp/1.0'})
session.auth = ('user', 'pass')

# 发送请求
response1 = session.get('https://httpbin.org/cookies/set/session_id/12345')
response2 = session.get('https://httpbin.org/cookies')
print(response2.json())  # cookies 被保留

# 关闭会话
session.close()

# 或使用上下文管理器
with requests.Session() as session:
    response = session.get('https://httpbin.org/get')
```

### 认证

```python
import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

# 基本认证
response = requests.get(
    'https://httpbin.org/basic-auth/user/pass',
    auth=HTTPBasicAuth('user', 'pass')
)

# 简写形式
response = requests.get(
    'https://httpbin.org/basic-auth/user/pass',
    auth=('user', 'pass')
)

# Digest 认证
response = requests.get(
    'https://httpbin.org/digest-auth/auth/user/pass',
    auth=HTTPDigestAuth('user', 'pass')
)

# 自定义认证
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    def __init__(self, token):
        self.token = token
    
    def __call__(self, r):
        r.headers['Authorization'] = f'Bearer {self.token}'
        return r

response = requests.get(
    'https://api.example.com/data',
    auth=TokenAuth('my_token')
)
```

### 超时和重试

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# 设置超时
response = requests.get('https://httpbin.org/delay/5', timeout=3)  # 3秒超时

# 分别设置连接和读取超时
response = requests.get(
    'https://httpbin.org/get',
    timeout=(3.05, 27)  # 连接超时3.05秒，读取超时27秒
)

# 自动重试
session = requests.Session()
retry = Retry(
    total=3,              # 总重试次数
    backoff_factor=1,     # 重试间隔
    status_forcelist=[500, 502, 503, 504]  # 需要重试的状态码
)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

response = session.get('https://httpbin.org/status/500')
```

### 代理

```python
import requests

# 设置代理
proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080',
}

response = requests.get('https://httpbin.org/ip', proxies=proxies)

# 带认证的代理
proxies = {
    'http': 'http://user:pass@10.10.1.10:3128',
}

# 使用 SOCKS 代理（需要 pip install requests[socks]）
proxies = {
    'http': 'socks5://user:pass@host:port',
    'https': 'socks5://user:pass@host:port',
}
```

### SSL 证书验证

```python
import requests

# 禁用证书验证（不推荐）
response = requests.get('https://httpbin.org/get', verify=False)

# 使用自定义 CA 证书
response = requests.get('https://httpbin.org/get', verify='/path/to/certfile')

# 客户端证书
response = requests.get(
    'https://httpbin.org/get',
    cert=('/path/client.cert', '/path/client.key')
)
```

## 0x05. 实际应用

### 封装请求工具

```python
import requests
from typing import Optional, Dict, Any
from dataclasses import dataclass

@dataclass
class APIResponse:
    success: bool
    status_code: int
    data: Any = None
    error: Optional[str] = None

class APIClient:
    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    
    def get(self, endpoint: str, params: Dict = None) -> APIResponse:
        try:
            response = self.session.get(
                f'{self.base_url}/{endpoint.lstrip("/")}',
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()
            return APIResponse(
                success=True,
                status_code=response.status_code,
                data=response.json()
            )
        except requests.exceptions.RequestException as e:
            return APIResponse(
                success=False,
                status_code=getattr(e.response, 'status_code', 0),
                error=str(e)
            )
    
    def post(self, endpoint: str, data: Dict = None) -> APIResponse:
        try:
            response = self.session.post(
                f'{self.base_url}/{endpoint.lstrip("/")}',
                json=data,
                timeout=self.timeout
            )
            response.raise_for_status()
            return APIResponse(
                success=True,
                status_code=response.status_code,
                data=response.json()
            )
        except requests.exceptions.RequestException as e:
            return APIResponse(
                success=False,
                status_code=getattr(e.response, 'status_code', 0),
                error=str(e)
            )
    
    def set_auth_token(self, token: str):
        self.session.headers['Authorization'] = f'Bearer {token}'

# 使用
client = APIClient('https://api.example.com')
response = client.get('/users')
if response.success:
    print(response.data)
else:
    print(f'错误: {response.error}')
```

### 文件下载

```python
import requests
from pathlib import Path

def download_file(url: str, save_path: str, chunk_size: int = 8192):
    """下载文件并显示进度"""
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    total_size = int(response.headers.get('content-length', 0))
    downloaded = 0
    
    with open(save_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                f.write(chunk)
                downloaded += len(chunk)
                if total_size:
                    progress = (downloaded / total_size) * 100
                    print(f'\r下载进度: {progress:.1f}%', end='')
    
    print(f'\n文件已保存到: {save_path}')

# 使用
download_file(
    'https://example.com/file.zip',
    'downloads/file.zip'
)
```

### 并发请求

```python
import asyncio
import aiohttp
from typing import List

async def fetch_url(session: aiohttp.ClientSession, url: str) -> str:
    """异步获取 URL 内容"""
    async with session.get(url) as response:
        return await response.text()

async def fetch_all(urls: List[str]) -> List[str]:
    """并发获取多个 URL"""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)

# 使用
urls = [
    'https://httpbin.org/delay/1',
    'https://httpbin.org/delay/2',
    'https://httpbin.org/delay/3'
]

results = asyncio.run(fetch_all(urls))
print(f'获取了 {len(results)} 个页面')
```

## 参考
1. [Requests 官方文档](https://docs.python-requests.org/)
2. [Requests GitHub](https://github.com/psf/requests)
3. [aiohttp 文档](https://docs.aiohttp.org/)