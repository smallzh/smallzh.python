# turtle，海龟绘图

有趣的Python模块，通过控制海龟在屏幕上移动来绘制图形。

参考[https://docs.python.org/3/library/turtle.html](https://docs.python.org/3/library/turtle.html)

## 0x01. 基本使用

```python
import turtle

# 创建画布和海龟
screen = turtle.Screen()  # 画布
t = turtle.Turtle()       # 海龟

# 基本移动
t.forward(100)   # 向前移动100像素
t.right(90)      # 右转90度
t.forward(100)
t.left(90)       # 左转90度
t.backward(50)   # 向后移动50像素

# 保持窗口打开
turtle.done()
```

## 0x02. 绘制基本图形

### 正方形

```python
import turtle

t = turtle.Turtle()

# 绘制正方形
for _ in range(4):
    t.forward(100)
    t.right(90)

turtle.done()
```

### 三角形

```python
import turtle

t = turtle.Turtle()

# 绘制等边三角形
for _ in range(3):
    t.forward(100)
    t.left(120)

turtle.done()
```

### 圆形

```python
import turtle

t = turtle.Turtle()

# 绘制圆形
t.circle(50)  # 半径50

# 绘制半圆
t.circle(50, 180)  # 半径50，角度180度

turtle.done()
```

### 多边形

```python
import turtle

t = turtle.Turtle()

def draw_polygon(sides, length):
    """绘制正多边形"""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

# 绘制五边形
draw_polygon(5, 100)

# 绘制六边形
t.penup()
t.goto(150, 0)
t.pendown()
draw_polygon(6, 80)

turtle.done()
```

## 0x03. 海龟控制

### 移动控制

```python
import turtle

t = turtle.Turtle()

# 绝对位置移动
t.goto(100, 100)    # 移动到 (100, 100)
t.setx(200)         # 设置 x 坐标
t.sety(50)          # 设置 y 坐标
t.home()            # 回到原点 (0, 0)

# 相对位置移动
t.forward(100)      # 向前
t.backward(50)      # 向后
t.left(90)          # 左转
t.right(45)         # 右转

# 抬笔和落笔
t.penup()           # 抬笔（移动时不画线）
t.goto(100, 100)
t.pendown()         # 落笔（开始画线）
t.forward(100)

turtle.done()
```

### 画笔控制

```python
import turtle

t = turtle.Turtle()

# 设置画笔颜色
t.pencolor('red')           # 颜色名称
t.pencolor('#FF0000')       # 十六进制
t.pencolor((1, 0, 0))       # RGB 元组

# 设置填充颜色
t.fillcolor('blue')
t.begin_fill()              # 开始填充
t.circle(50)
t.end_fill()                # 结束填充

# 同时设置画笔和填充颜色
t.color('green', 'yellow')

# 设置画笔粗细
t.pensize(5)                # 画笔宽度为5像素

# 设置画笔速度
t.speed(0)                  # 最快 (0-10)
t.speed('fastest')          # 最快
t.speed('slow')             # 慢速

turtle.done()
```

### 海龟外观

```python
import turtle

t = turtle.Turtle()

# 设置海龟形状
t.shape('turtle')   # 海龟形状
t.shape('circle')   # 圆形
t.shape('square')   # 正方形
t.shape('arrow')    # 箭头（默认）
t.shape('triangle') # 三角形

# 显示/隐藏海龟
t.hideturtle()      # 隐藏海龟
t.showturtle()      # 显示海龟

turtle.done()
```

## 0x04. 高级绘图

### 螺旋线

```python
import turtle

t = turtle.Turtle()
t.speed(0)

# 绘制螺旋线
for i in range(100):
    t.forward(i * 2)
    t.right(91)

turtle.done()
```

### 彩虹螺旋

```python
import turtle

t = turtle.Turtle()
t.speed(0)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for i in range(360):
    t.pencolor(colors[i % 6])
    t.pensize(i / 100 + 1)
    t.forward(i)
    t.right(59)

turtle.done()
```

### 分形树

```python
import turtle

def draw_tree(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_tree(branch_length - 15, t)
        t.left(40)
        draw_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

t = turtle.Turtle()
t.speed(0)
t.left(90)
t.backward(100)

draw_tree(75, t)
turtle.done()
```

### 星星

```python
import turtle

t = turtle.Turtle()
t.speed(0)

def draw_star(size):
    """绘制五角星"""
    for _ in range(5):
        t.forward(size)
        t.right(144)

# 绘制多个星星
for i in range(5):
    t.penup()
    t.goto(-200 + i * 100, 0)
    t.pendown()
    draw_star(50)

turtle.done()
```

### 万花尺

```python
import turtle
import math

t = turtle.Turtle()
t.speed(0)

def spirograph(R, r, d):
    """绘制万花尺图案"""
    t.penup()
    t.goto(R - r + d, 0)
    t.pendown()
    
    for i in range(360 * r // math.gcd(R, r)):
        angle = math.radians(i)
        x = (R - r) * math.cos(angle) + d * math.cos((R - r) / r * angle)
        y = (R - r) * math.sin(angle) - d * math.sin((R - r) / r * angle)
        t.goto(x, y)

spirograph(100, 30, 50)
turtle.done()
```

## 0x05. 文本绘制

```python
import turtle

t = turtle.Turtle()

# 绘制文本
t.write("Hello, Turtle!", font=("Arial", 16, "bold"))

# 移动后绘制
t.penup()
t.goto(0, -50)
t.pendown()
t.write("Python绘图", font=("SimHei", 20, "normal"))

turtle.done()
```

## 0x06. 事件处理

```python
import turtle

screen = turtle.Screen()
t = turtle.Turtle()

def move_forward():
    t.forward(20)

def turn_left():
    t.left(30)

def turn_right():
    t.right(30)

# 绑定键盘事件
screen.onkey(move_forward, "Up")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.listen()  # 开始监听

turtle.done()
```

## 0x07. 实用示例

### 绘制太极图

```python
import turtle

def draw_yin_yang(radius):
    """绘制太极图"""
    t = turtle.Turtle()
    t.speed(0)
    
    # 绘制左半圆（黑色）
    t.color("black", "black")
    t.begin_fill()
    t.circle(radius, 180)
    t.circle(radius * 0.5, 180)
    t.circle(-radius * 0.5, 180)
    t.end_fill()
    
    # 绘制右半圆（白色）
    t.color("black", "white")
    t.begin_fill()
    t.circle(radius, 180)
    t.circle(-radius * 0.5, 180)
    t.circle(radius * 0.5, 180)
    t.end_fill()
    
    # 绘制小圆点
    t.penup()
    t.goto(0, radius * 0.5)
    t.pendown()
    t.color("white", "white")
    t.begin_fill()
    t.circle(radius * 0.15)
    t.end_fill()
    
    t.penup()
    t.goto(0, -radius * 0.5)
    t.pendown()
    t.color("black", "black")
    t.begin_fill()
    t.circle(radius * 0.15)
    t.end_fill()

draw_yin_yang(100)
turtle.done()
```

### 绘制 Mandelbrot 集

```python
import turtle

def mandelbrot(c, max_iter):
    """计算 Mandelbrot 迭代次数"""
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter

screen = turtle.Screen()
screen.setup(800, 600)
screen.setworldcoordinates(-2, -1.5, 1, 1.5)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

max_iter = 50
for x in range(-400, 400, 10):
    for y in range(-300, 300, 10):
        c = complex(x / 200, y / 200)
        m = mandelbrot(c, max_iter)
        color = 1 - m / max_iter
        t.penup()
        t.goto(x / 200, y / 200)
        t.pendown()
        t.pencolor((color, color, color))
        t.dot(5)

turtle.done()
```

## 附
1. [https://en.wikipedia.org/wiki/Turtle_(robot)](https://en.wikipedia.org/wiki/Turtle_(robot))
2. [Python 官方文档 - turtle 模块](https://docs.python.org/3/library/turtle.html)