# 和数学计算相关的库

Python 提供了丰富的数学计算库，从基础数学运算到高级科学计算。

## 0x01. 内置数学函数

Python 内置了一些基本的数学函数：

```python
# 基本数学运算
print(abs(-5))          # 5 (绝对值)
print(round(3.14159, 2)) # 3.14 (四舍五入)
print(pow(2, 3))        # 8 (幂运算)
print(divmod(10, 3))    # (3, 1) (商和余数)

# 最大最小值
print(max(1, 2, 3))     # 3
print(min(1, 2, 3))     # 1
print(sum([1, 2, 3]))   # 6

# 三角函数（需要 import math）
import math
print(math.sqrt(16))    # 4.0 (平方根)
print(math.ceil(3.2))   # 4 (向上取整)
print(math.floor(3.8))  # 3 (向下取整)
print(math.pi)          # 3.141592653589793
print(math.e)           # 2.718281828459045
```

## 0x02. math 模块

```python
import math

# 三角函数
print(math.sin(math.pi / 2))  # 1.0
print(math.cos(0))            # 1.0
print(math.tan(math.pi / 4))  # 1.0

# 反三角函数
print(math.asin(1))           # π/2
print(math.acos(0))           # π/2
print(math.atan(1))           # π/4

# 双曲函数
print(math.sinh(1))
print(math.cosh(1))
print(math.tanh(1))

# 对数函数
print(math.log(10))           # 自然对数
print(math.log10(100))        # 以10为底的对数
print(math.log2(8))           # 以2为底的对数

# 指数函数
print(math.exp(1))            # e^1
print(math.expm1(1))          # e^1 - 1 (精度更高)

# 阶乘和组合
print(math.factorial(5))      # 120
print(math.comb(10, 3))       # 120 (组合数)
print(math.perm(10, 3))       # 720 (排列数)

# 最大公约数和最小公倍数
print(math.gcd(12, 8))        # 4
print(math.lcm(12, 8))        # 24 (Python 3.9+)

# 浮点数操作
print(math.isfinite(1.0))     # True
print(math.isinf(float('inf'))) # True
print(math.isnan(float('nan'))) # True
```

## 0x03. NumPy

NumPy 是 Python 中科学计算的基础库，提供了高性能的多维数组对象和数学函数。

```shell
pip install numpy
```

### 数组创建

```python
import numpy as np

# 从列表创建数组
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# 特殊数组
zeros = np.zeros((3, 3))          # 全0数组
ones = np.ones((2, 4))            # 全1数组
full = np.full((2, 2), 7)         # 指定值填充
eye = np.eye(3)                   # 单位矩阵
arange = np.arange(0, 10, 2)     # 等差数列
linspace = np.linspace(0, 1, 5)  # 等间隔数组

print(arr1)        # [1 2 3 4 5]
print(arr2.shape)  # (2, 3)
print(arr2.dtype)  # int64
```

### 数组操作

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

# 索引和切片
print(arr[0, 1])      # 2
print(arr[:, 1])      # [2 5] (第二列)
print(arr[1, :])      # [4 5 6] (第二行)

# 形状操作
print(arr.reshape(3, 2))  # 改变形状
print(arr.T)              # 转置
print(arr.flatten())      # 展平

# 数组拼接
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.concatenate([a, b]))          # [1 2 3 4 5 6]
print(np.stack([a, b]))                # [[1 2 3], [4 5 6]]
print(np.hstack([a, b]))               # 水平拼接
print(np.vstack([[a], [b]]))           # 垂直拼接
```

### 数学运算

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 元素级运算
print(a + b)          # [5 7 9]
print(a * b)          # [4 10 18]
print(a ** 2)         # [1 4 9]
print(np.sqrt(a))     # [1.0, 1.414, 1.732]

# 矩阵运算
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))   # 矩阵乘法
print(A @ B)          # 矩阵乘法（Python 3.5+）

# 聚合函数
print(np.sum(a))      # 6
print(np.mean(a))     # 2.0
print(np.std(a))      # 标准差
print(np.max(a))      # 3
print(np.min(a))      # 1
print(np.argmax(a))   # 最大值索引
```

### 广播机制

```python
import numpy as np

# 数组与标量运算
arr = np.array([1, 2, 3])
print(arr * 2)        # [2 4 6]

# 不同形状数组运算
a = np.array([[1], [2], [3]])  # (3, 1)
b = np.array([10, 20, 30])     # (3,)
print(a + b)          # [[11, 21, 31], [12, 22, 32], [13, 23, 33]]
```

### 随机数生成

```python
import numpy as np

# 设置随机种子
np.random.seed(42)

# 各种分布
print(np.random.rand(3, 3))        # 均匀分布 [0, 1)
print(np.random.randn(3, 3))       # 标准正态分布
print(np.random.randint(0, 10, 5)) # 随机整数
print(np.random.choice([1, 2, 3, 4, 5], 3))  # 随机选择

# 正态分布
print(np.random.normal(loc=0, scale=1, size=1000))

# 排列
arr = np.array([1, 2, 3, 4, 5])
print(np.random.permutation(arr))  # 随机排列
np.random.shuffle(arr)             # 原地打乱
```

## 0x04. SciPy

SciPy 建立在 NumPy 之上，提供了更多的科学计算功能。

```shell
pip install scipy
```

### 线性代数

```python
from scipy import linalg
import numpy as np

# 矩阵分解
A = np.array([[1, 2], [3, 4]])
P, L, U = linalg.lu(A)  # LU分解
print(f"L:\n{L}")
print(f"U:\n{U}")

# 特征值和特征向量
eigenvalues, eigenvectors = linalg.eig(A)
print(f"特征值: {eigenvalues}")
print(f"特征向量:\n{eigenvectors}")

# 矩阵求逆
A_inv = linalg.inv(A)
print(f"逆矩阵:\n{A_inv}")

# 行列式
det = linalg.det(A)
print(f"行列式: {det}")

# 奇异值分解
U, s, Vh = linalg.svd(A)
```

### 优化

```python
from scipy import optimize

# 最小化函数
def f(x):
    return (x - 2) ** 2 + 1

result = optimize.minimize(f, x0=0)
print(f"最小值点: {result.x}")    # [2.]
print(f"最小值: {result.fun}")    # 1.0

# 约束优化
def objective(x):
    return x[0]**2 + x[1]**2

def constraint(x):
    return x[0] + x[1] - 1

constraints = {'type': 'eq', 'fun': constraint}
result = optimize.minimize(objective, x0=[0, 0], constraints=constraints)
print(f"最优解: {result.x}")

# 曲线拟合
from scipy.optimize import curve_fit
import numpy as np

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

x_data = np.linspace(0, 4, 50)
y_data = func(x_data, 2.5, 1.3, 0.5) + 0.2 * np.random.normal(size=50)

popt, pcov = curve_fit(func, x_data, y_data)
print(f"拟合参数: {popt}")
```

### 积分

```python
from scipy import integrate
import numpy as np

# 定积分
result, error = integrate.quad(lambda x: x**2, 0, 1)
print(f"积分结果: {result}, 误差: {error}")

# 二重积分
def integrand(y, x):
    return x * y**2

result, error = integrate.dblquad(integrand, 0, 1, lambda x: 0, lambda x: 1)
print(f"二重积分: {result}")

# 常微分方程
from scipy.integrate import odeint

def model(y, t):
    k = 0.3
    dydt = -k * y
    return dydt

y0 = 5
t = np.linspace(0, 20, 100)
solution = odeint(model, y0, t)
```

### 信号处理

```python
from scipy import signal
import numpy as np

# 滤波器设计
b, a = signal.butter(4, 100, fs=1000, btype='low')
w, h = signal.freqs(b, a)

# 信号滤波
t = np.linspace(0, 1, 1000, False)
sig = np.sin(2 * np.pi * 10 * t) + np.sin(2 * np.pi * 20 * t)
filtered = signal.filtfilt(b, a, sig)

# 卷积
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
conv = signal.convolve(x, y)
```

## 0x05. SymPy

SymPy 是 Python 的符号数学库，可以进行符号计算。

```shell
pip install sympy
```

### 基本符号运算

```python
from sympy import *

# 定义符号
x, y, z = symbols('x y z')

# 符号表达式
expr = x**2 + 2*x + 1
print(expr)
print(expand((x + 1)**2))     # 展开
print(factor(x**2 + 2*x + 1)) # 因式分解

# 简化
print(simplify(sin(x)**2 + cos(x)**2))  # 1

# 代入值
expr = x**2 + 2*x + 1
print(expr.subs(x, 2))  # 9
```

### 微积分

```python
from sympy import *

x = symbols('x')

# 求导
print(diff(x**3, x))          # 3*x**2
print(diff(sin(x), x))        # cos(x)
print(diff(exp(x), x))        # exp(x)

# 积分
print(integrate(x**2, x))     # x**3/3
print(integrate(x**2, (x, 0, 1)))  # 1/3 (定积分)
print(integrate(exp(-x), (x, 0, oo)))  # 1

# 极限
print(limit(sin(x)/x, x, 0))  # 1
print(limit(1/x, x, oo))      # 0

# 级数展开
print(series(sin(x), x, 0, 6))  # x - x**3/6 + x**5/120 + O(x**6)
```

### 方程求解

```python
from sympy import *

x, y = symbols('x y')

# 代数方程
print(solve(x**2 - 4, x))       # [-2, 2]
print(solve(x**2 + x + 1, x))   # 复数解

# 方程组
print(solve([x + y - 2, x - y - 0], [x, y]))  # {x: 1, y: 1}

# 微分方程
f = Function('f')
print(dsolve(f(x).diff(x) - f(x), f(x)))  # f(x) = C1*exp(x)
```

### 矩阵运算

```python
from sympy import Matrix

A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])

print(A * B)          # 矩阵乘法
print(A.T)            # 转置
print(A.inv())        # 逆矩阵
print(A.det())        # 行列式
print(A.eigenvals())  # 特征值
```

## 0x06. Matplotlib

Matplotlib 是 Python 中最流行的绘图库。

```shell
pip install matplotlib
```

### 基本绘图

```python
import matplotlib.pyplot as plt
import numpy as np

# 折线图
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('正弦函数')
plt.legend()
plt.grid(True)
plt.show()

# 多条线
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.legend()
plt.show()

# 散点图
x = np.random.randn(100)
y = np.random.randn(100)
plt.scatter(x, y, alpha=0.5)
plt.show()

# 柱状图
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]
plt.bar(categories, values)
plt.show()

# 饼图
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()
```

### 子图

```python
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 第一个子图
axes[0, 0].plot([1, 2, 3], [1, 4, 9])
axes[0, 0].set_title('线性')

# 第二个子图
axes[0, 1].plot([1, 2, 3], [1, 2, 3])
axes[0, 1].set_title('二次')

# 第三个子图
x = np.linspace(0, 10, 100)
axes[1, 0].plot(x, np.sin(x))
axes[1, 0].set_title('sin')

# 第四个子图
axes[1, 1].plot(x, np.cos(x))
axes[1, 1].set_title('cos')

plt.tight_layout()
plt.show()
```

### 3D 绘图

```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 曲面图
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

ax.plot_surface(X, Y, Z, cmap='viridis')
plt.show()

# 散点图
x = np.random.randn(100)
y = np.random.randn(100)
z = np.random.randn(100)
ax.scatter(x, y, z)
plt.show()
```

## 0x07. Pandas

Pandas 提供了数据分析和处理的高性能数据结构。

```shell
pip install pandas
```

### 数据操作

```python
import pandas as pd
import numpy as np

# Series
s = pd.Series([1, 2, 3, 4, 5])
print(s.mean())    # 3.0
print(s.std())     # 标准差

# DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# 统计
print(df.describe())
print(df.mean())
print(df.corr())  # 相关系数

# 分组统计
df = pd.DataFrame({
    'category': ['A', 'B', 'A', 'B', 'A'],
    'value': [10, 20, 30, 40, 50]
})
print(df.groupby('category').mean())

# 窗口函数
df = pd.DataFrame({'value': range(10)})
df['rolling_mean'] = df['value'].rolling(window=3).mean()
```

## 参考
1. [Python math 模块文档](https://docs.python.org/3/library/math.html)
2. [NumPy 官方文档](https://numpy.org/doc/)
3. [SciPy 官方文档](https://docs.scipy.org/doc/scipy/)
4. [SymPy 官方文档](https://docs.sympy.org/)
5. [Matplotlib 官方文档](https://matplotlib.org/stable/contents.html)
6. [Pandas 官方文档](https://pandas.pydata.org/docs/)
7. [概率论和数理统计](https://zhuanlan.zhihu.com/p/539614760)