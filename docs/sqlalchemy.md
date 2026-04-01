# SQLAlchemy

SQLAlchemy 是 Python 中最流行的 SQL 工具包和对象关系映射（ORM）框架，提供原生 SQL 和 ORM 两种处理方式。

官网：[https://www.sqlalchemy.org/](https://www.sqlalchemy.org/)

## 0x01. 安装

```shell
pip install sqlalchemy

# 安装数据库驱动
pip install pymysql      # MySQL
pip install psycopg2     # PostgreSQL
pip install sqlite3      # SQLite (Python 内置)
```

## 0x02. 核心概念

SQLAlchemy 提供了两种使用方式：
- **SQLAlchemy Core**：直接使用 SQL 表达式语言
- **SQLAlchemy ORM**：使用对象关系映射

## 0x03. SQLAlchemy Core

### 创建引擎和连接

```python
from sqlalchemy import create_engine

# 创建引擎
# SQLite
engine = create_engine('sqlite:///mydb.db', echo=True)

# MySQL
engine = create_engine('mysql+pymysql://user:password@localhost:3306/mydb')

# PostgreSQL
engine = create_engine('postgresql+psycopg2://user:password@localhost:5432/mydb')

# 获取连接
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM users"))
    for row in result:
        print(row)
```

### 定义表结构

```python
from sqlalchemy import MetaData, Table, Column, Integer, String, Float, DateTime
from sqlalchemy import ForeignKey, Boolean, Text

metadata = MetaData()

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50), nullable=False),
    Column('email', String(100), unique=True),
    Column('age', Integer),
    Column('active', Boolean, default=True),
    Column('created_at', DateTime)
)

posts = Table('posts', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(200), nullable=False),
    Column('content', Text),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('created_at', DateTime)
)

# 创建表
metadata.create_all(engine)
```

### 插入数据

```python
from sqlalchemy import insert
from datetime import datetime

# 单条插入
with engine.connect() as conn:
    stmt = insert(users).values(
        name='Alice',
        email='alice@example.com',
        age=25,
        created_at=datetime.now()
    )
    result = conn.execute(stmt)
    conn.commit()
    print(f'插入ID: {result.inserted_primary_key}')

# 批量插入
with engine.connect() as conn:
    data = [
        {'name': 'Bob', 'email': 'bob@example.com', 'age': 30},
        {'name': 'Charlie', 'email': 'charlie@example.com', 'age': 35},
        {'name': 'David', 'email': 'david@example.com', 'age': 28}
    ]
    stmt = insert(users)
    result = conn.execute(stmt, data)
    conn.commit()
    print(f'插入 {result.rowcount} 条记录')
```

### 查询数据

```python
from sqlalchemy import select

with engine.connect() as conn:
    # 查询所有
    stmt = select(users)
    result = conn.execute(stmt)
    for row in result:
        print(row)
    
    # 查询特定列
    stmt = select(users.c.name, users.c.email)
    result = conn.execute(stmt)
    for row in result:
        print(f'{row.name}: {row.email}')
    
    # 带条件查询
    stmt = select(users).where(users.c.age > 25)
    result = conn.execute(stmt)
    
    # 多条件查询
    stmt = select(users).where(
        (users.c.age > 25) & (users.c.active == True)
    )
    
    # 排序
    stmt = select(users).order_by(users.c.age.desc())
    
    # 限制结果数量
    stmt = select(users).limit(10).offset(20)
    
    # 聚合函数
    from sqlalchemy import func
    stmt = select(func.count(users.c.id), func.avg(users.c.age))
    result = conn.execute(stmt).first()
    print(f'总数: {result[0]}, 平均年龄: {result[1]}')
```

### 更新数据

```python
from sqlalchemy import update

with engine.connect() as conn:
    # 更新单条记录
    stmt = update(users).where(users.c.name == 'Alice').values(age=26)
    result = conn.execute(stmt)
    conn.commit()
    print(f'更新 {result.rowcount} 条记录')
    
    # 条件更新
    stmt = update(users).where(users.c.age < 30).values(active=True)
    conn.execute(stmt)
    conn.commit()
```

### 删除数据

```python
from sqlalchemy import delete

with engine.connect() as conn:
    # 删除单条记录
    stmt = delete(users).where(users.c.name == 'Alice')
    result = conn.execute(stmt)
    conn.commit()
    print(f'删除 {result.rowcount} 条记录')
    
    # 条件删除
    stmt = delete(users).where(users.c.age < 25)
    conn.execute(stmt)
    conn.commit()
```

### 连接查询

```python
from sqlalchemy import join

with engine.connect() as conn:
    # INNER JOIN
    stmt = select(users, posts).select_from(
        users.join(posts, users.c.id == posts.c.user_id)
    )
    result = conn.execute(stmt)
    for row in result:
        print(f'{row.name}: {row.title}')
    
    # LEFT JOIN
    stmt = select(users, posts).select_from(
        users.outerjoin(posts, users.c.id == posts.c.user_id)
    )
```

## 0x04. SQLAlchemy ORM

### 配置

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 创建基类
Base = declarative_base()

# 创建引擎
engine = create_engine('sqlite:///mydb.db', echo=True)

# 创建会话工厂
Session = sessionmaker(bind=engine)
session = Session()
```

### 定义模型

```python
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    
    # 关系
    posts = relationship('Post', back_populates='author')
    
    def __repr__(self):
        return f'<User(name={self.name}, email={self.email})>'

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)
    
    # 关系
    author = relationship('User', back_populates='posts')
    
    def __repr__(self):
        return f'<Post(title={self.title})>'

# 创建表
Base.metadata.create_all(engine)
```

### CRUD 操作

```python
# 创建
def create_user(name, email, age):
    user = User(name=name, email=email, age=age)
    session.add(user)
    session.commit()
    return user

# 批量创建
def create_users(users_data):
    users = [User(**data) for data in users_data]
    session.add_all(users)
    session.commit()

# 查询
def get_user_by_id(user_id):
    return session.query(User).get(user_id)

def get_all_users():
    return session.query(User).all()

def get_users_by_age(min_age):
    return session.query(User).filter(User.age >= min_age).all()

def get_user_by_email(email):
    return session.query(User).filter_by(email=email).first()

# 复杂查询
def get_active_users_ordered_by_age():
    return session.query(User).filter(
        User.active == True
    ).order_by(User.age.desc()).all()

# 聚合查询
def get_user_count():
    from sqlalchemy import func
    return session.query(func.count(User.id)).scalar()

def get_average_age():
    from sqlalchemy import func
    return session.query(func.avg(User.age)).scalar()

# 更新
def update_user(user_id, **kwargs):
    user = session.query(User).get(user_id)
    if user:
        for key, value in kwargs.items():
            setattr(user, key, value)
        session.commit()
    return user

# 删除
def delete_user(user_id):
    user = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()
        return True
    return False

# 使用示例
user = create_user('Alice', 'alice@example.com', 25)
print(user)

users = get_users_by_age(25)
for u in users:
    print(u)

update_user(user.id, age=26)
delete_user(user.id)
```

### 关系查询

```python
# 创建带关系的数据
def create_user_with_posts():
    user = User(name='Bob', email='bob@example.com', age=30)
    
    post1 = Post(title='第一篇文章', content='这是内容', author=user)
    post2 = Post(title='第二篇文章', content='更多内容', author=user)
    
    session.add(user)
    session.commit()
    return user

# 查询关系
def get_user_posts(user_id):
    user = session.query(User).get(user_id)
    return user.posts

def get_post_author(post_id):
    post = session.query(Post).get(post_id)
    return post.author

# 预加载（避免 N+1 查询）
def get_users_with_posts():
    from sqlalchemy.orm import joinedload
    return session.query(User).options(joinedload(User.posts)).all()
```

### 事务处理

```python
def transfer_money(from_user_id, to_user_id, amount):
    """示例：转账操作"""
    try:
        from_user = session.query(User).get(from_user_id)
        to_user = session.query(User).get(to_user_id)
        
        # 假设有 balance 字段
        # from_user.balance -= amount
        # to_user.balance += amount
        
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f'事务失败: {e}')
        return False
```

## 0x05. 常用查询技巧

```python
from sqlalchemy import and_, or_, not_

# 复杂条件查询
users = session.query(User).filter(
    and_(
        User.age >= 18,
        or_(User.name == 'Alice', User.name == 'Bob'),
        not_(User.active == False)
    )
).all()

# 模糊查询
users = session.query(User).filter(User.name.like('%li%')).all()
users = session.query(User).filter(User.name.ilike('%alice%')).all()  # 不区分大小写

# 范围查询
users = session.query(User).filter(User.age.between(20, 30)).all()
users = session.query(User).filter(User.age.in_([25, 30, 35])).all()

# 空值查询
users = session.query(User).filter(User.email == None).all()
users = session.query(User).filter(User.email != None).all()

# 分页查询
page = 1
per_page = 10
users = session.query(User).offset((page-1)*per_page).limit(per_page).all()

# 分组统计
from sqlalchemy import func
stats = session.query(
    User.age,
    func.count(User.id).label('count')
).group_by(User.age).having(func.count(User.id) > 1).all()

for stat in stats:
    print(f'年龄 {stat.age}: {stat.count} 人')
```

## 参考
1. [SQLAlchemy 官方文档](https://docs.sqlalchemy.org/)
2. [SQLAlchemy ORM 教程](https://docs.sqlalchemy.org/en/20/orm/tutorial.html)
3. [SQLAlchemy Core 教程](https://docs.sqlalchemy.org/en/20/core/tutorial.html)