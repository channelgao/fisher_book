"""
coding:utf-8
@Software : PyCharm
@File : base.py
@Time : 2023/3/17 17:03
@Author : Ryan Gao
@Email : 
@description : 
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, SmallInteger, Integer

# 初始化 SQLAlchemy 对象
db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    
    create_time = Column('create_time', Integer)
    delete_status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != id:
                setattr(self, key, value)