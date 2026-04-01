# Streamlit 使用

Streamlit 是一个开源的 Python 库，可以快速创建数据应用和机器学习模型的 Web 界面。

官网：[https://streamlit.io/](https://streamlit.io/)，文档地址：[https://docs.streamlit.io/](https://docs.streamlit.io/)

## 0x01. 安装和启动

```shell
# 安装
pip install streamlit

# 启动应用
streamlit run app.py

# 指定端口
streamlit run app.py --server.port 8080

# 关闭统计信息
streamlit run app.py --browser.gatherUsageStats false
```

## 0x02. 基本组件

### 文本显示

```python
import streamlit as st

# 标题
st.title('我的第一个 Streamlit 应用')
st.header('这是一个标题')
st.subheader('这是一个子标题')

# 文本
st.text('这是普通文本')
st.markdown('**这是粗体文本**，*这是斜体文本*')
st.latex(r'E = mc^2')

# 代码显示
st.code('''
def hello():
    print("Hello, World!")
''', language='python')
```

### 数据显示

```python
import streamlit as st
import pandas as pd
import numpy as np

# DataFrame
df = pd.DataFrame({
    '姓名': ['Alice', 'Bob', 'Charlie'],
    '年龄': [25, 30, 35],
    '城市': ['北京', '上海', '广州']
})

st.dataframe(df)  # 交互式表格
st.table(df)      # 静态表格
st.json({'name': 'Alice', 'age': 25})  # JSON 显示

# 指标
st.metric(label="温度", value="25°C", delta="+2°C")
st.metric(label="股价", value="150元", delta="-5元", delta_color="inverse")
```

### 图表

```python
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 内置图表
df = pd.DataFrame(np.random.randn(100, 2), columns=['x', 'y'])
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

# Matplotlib 图表
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
st.pyplot(fig)

# Plotly 图表（需要安装 plotly）
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
st.plotly_chart(fig)

# Altair 图表（需要安装 altair）
import altair as alt
chart = alt.Chart(df).mark_circle().encode(
    x='sepal_width',
    y='sepal_length',
    color='species'
)
st.altair_chart(chart, use_container_width=True)
```

### 多媒体

```python
import streamlit as st

# 图片
st.image('image.png', caption='图片说明', use_container_width=True)

# 音频
st.audio('audio.mp3')

# 视频
st.video('video.mp4')
```

## 0x03. 输入组件

### 基本输入

```python
import streamlit as st

# 文本输入
name = st.text_input('请输入你的名字', '默认值')
password = st.text_input('密码', type='password')

# 数字输入
age = st.number_input('请输入年龄', min_value=0, max_value=120, value=25)
score = st.slider('选择分数', 0, 100, 50)

# 选择框
color = st.selectbox('选择颜色', ['红', '绿', '蓝'])
colors = st.multiselect('选择多个颜色', ['红', '绿', '蓝', '黄'])

# 单选和多选
option = st.radio('选择一个选项', ['选项1', '选项2', '选项3'])
options = st.multiselect('选择多个选项', ['选项1', '选项2', '选项3'])

# 复选框
agree = st.checkbox('我同意条款')

# 按钮
if st.button('点击我'):
    st.write('按钮被点击了！')

# 日期和时间
import datetime
date = st.date_input('选择日期', datetime.date.today())
time = st.time_input('选择时间', datetime.time(12, 0))

# 文件上传
uploaded_file = st.file_uploader('上传文件', type=['csv', 'txt', 'xlsx'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
```

### 高级输入

```python
import streamlit as st

# 颜色选择器
color = st.color_picker('选择颜色', '#00f900')
st.write(f'选择的颜色: {color}')

# 滑块范围
values = st.slider('选择范围', 0.0, 100.0, (25.0, 75.0))
st.write(f'选择的范围: {values}')

# 文本区域
text = st.text_area('输入长文本', height=200)

# 进度条
import time
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)
    time.sleep(0.01)

# 状态显示
with st.spinner('正在处理...'):
    time.sleep(2)
st.success('完成！')
st.error('这是一个错误')
st.warning('这是一个警告')
st.info('这是一个信息')
```

## 0x04. 布局

### 侧边栏

```python
import streamlit as st

# 侧边栏
st.sidebar.title('侧边栏')
st.sidebar.write('这是侧边栏内容')

# 侧边栏组件
name = st.sidebar.text_input('名字')
age = st.sidebar.slider('年龄', 0, 100, 25)

# 根据侧边栏输入显示主内容
st.write(f'你好，{name}！你今年 {age} 岁。')
```

### 列布局

```python
import streamlit as st

# 等宽列
col1, col2, col3 = st.columns(3)

with col1:
    st.header('第一列')
    st.write('这是第一列内容')

with col2:
    st.header('第二列')
    st.write('这是第二列内容')

with col3:
    st.header('第三列')
    st.write('这是第三列内容')

# 不等宽列
col1, col2 = st.columns([2, 1])
with col1:
    st.write('这是宽列')
with col2:
    st.write('这是窄列')
```

### 标签页

```python
import streamlit as st

tab1, tab2, tab3 = st.tabs(['Tab 1', 'Tab 2', 'Tab 3'])

with tab1:
    st.header('标签页 1')
    st.write('这是第一个标签页的内容')

with tab2:
    st.header('标签页 2')
    st.write('这是第二个标签页的内容')

with tab3:
    st.header('标签页 3')
    st.write('这是第三个标签页的内容')
```

### 展开器

```python
import streamlit as st

with st.expander('点击展开更多内容'):
    st.write('这是隐藏的内容')
    st.image('image.png')

# 默认展开
with st.expander('详情', expanded=True):
    st.write('默认展开的内容')
```

## 0x05. 状态管理

### 会话状态

```python
import streamlit as st

# 初始化状态
if 'count' not in st.session_state:
    st.session_state.count = 0

# 使用状态
st.write(f'计数: {st.session_state.count}')

if st.button('增加'):
    st.session_state.count += 1
    st.rerun()  # 重新运行脚本

if st.button('重置'):
    st.session_state.count = 0
    st.rerun()

# 复杂状态
if 'data' not in st.session_state:
    st.session_state.data = {
        'users': [],
        'current_user': None
    }

def add_user(name):
    st.session_state.data['users'].append(name)

name = st.text_input('用户名')
if st.button('添加用户') and name:
    add_user(name)
    st.success(f'用户 {name} 已添加')

st.write('用户列表:', st.session_state.data['users'])
```

### 缓存

```python
import streamlit as st
import pandas as pd
import time

# 缓存数据
@st.cache_data
def load_data():
    time.sleep(2)  # 模拟耗时操作
    return pd.DataFrame({
        'x': range(1000),
        'y': range(1000, 2000)
    })

# 第一次调用会执行，后续调用使用缓存
df = load_data()
st.write(df)

# 缓存资源（如数据库连接）
@st.cache_resource
def get_database_connection():
    import sqlalchemy
    return sqlalchemy.create_engine('sqlite:///mydb.db')

conn = get_database_connection()

# 清除缓存
if st.button('清除缓存'):
    st.cache_data.clear()
    st.cache_resource.clear()
    st.success('缓存已清除')
```

## 0x06. 回调函数

```python
import streamlit as st

def on_input_change():
    st.session_state.input_changed = True

def on_button_click():
    st.session_state.button_clicked = True

# 使用回调
st.text_input(
    '输入文本',
    key='text_input',
    on_change=on_input_change
)

st.button('提交', on_click=on_button_click)

# 显示状态
if st.session_state.get('input_changed'):
    st.write('输入已更改')

if st.session_state.get('button_clicked'):
    st.write('按钮已点击')
```

## 0x07. 实用示例

### 文件上传和处理

```python
import streamlit as st
import pandas as pd

st.title('CSV 文件分析器')

uploaded_file = st.file_uploader('上传 CSV 文件', type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader('数据预览')
    st.dataframe(df.head(10))
    
    st.subheader('数据统计')
    st.write(df.describe())
    
    st.subheader('列选择')
    columns = st.multiselect('选择要显示的列', df.columns.tolist(), default=df.columns.tolist())
    st.dataframe(df[columns])
    
    st.subheader('数据可视化')
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    if numeric_columns:
        x_col = st.selectbox('X 轴', numeric_columns)
        y_col = st.selectbox('Y 轴', numeric_columns)
        st.line_chart(df[[x_col, y_col]])
```

### 简单机器学习应用

```python
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.title('鸢尾花分类器')

# 加载数据
@st.cache_data
def load_data():
    from sklearn.datasets import load_iris
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    return df, iris.target_names

df, target_names = load_data()

# 显示数据
st.subheader('数据集')
st.dataframe(df)

# 训练模型
@st.cache_resource
def train_model():
    X = df.drop('target', axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    accuracy = accuracy_score(y_test, model.predict(X_test))
    return model, accuracy

model, accuracy = train_model()
st.write(f'模型准确率: {accuracy:.2%}')

# 预测
st.subheader('预测')
sepal_length = st.slider('花萼长度', 4.0, 8.0, 5.0)
sepal_width = st.slider('花萼宽度', 2.0, 4.5, 3.0)
petal_length = st.slider('花瓣长度', 1.0, 7.0, 4.0)
petal_width = st.slider('花瓣宽度', 0.1, 2.5, 1.0)

if st.button('预测'):
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    st.success(f'预测结果: {target_names[prediction[0]]}')
```

## 参考
1. [Streamlit 官方文档](https://docs.streamlit.io/)
2. [Streamlit API 参考](https://docs.streamlit.io/library/api-reference)
3. [Streamlit Gallery](https://streamlit.io/gallery)