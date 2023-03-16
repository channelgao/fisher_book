"""
coding:utf-8
@Software : PyCharm
@File : book.py
@Time : 2023/3/16 11:40
@Author : Ryan Gao
@Email :
@description : 
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Column

# 初始化 SQLAlchemy 对象
db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), nullable=True, default='佚名')
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    binding = Column(String(20))
    publisher = Column(String(50))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(100))

    def sample(self):
        pass
