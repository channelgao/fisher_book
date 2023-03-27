"""
coding:utf-8
@Software : PyCharm
@File : base.py
@Time : 2023/3/17 17:03
@Author : Ryan Gao
@Email : 
@description : 
"""
import time

from contextlib import contextmanager
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, SmallInteger, Integer
from sqlalchemy.exc import OperationalError


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


# 重写filter_by方法
class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'delete_status' not in kwargs.keys():
            kwargs['delete_status'] = 1
        return super().filter_by(**kwargs)


# 初始化 SQLAlchemy 对象 子类
try:
    db = SQLAlchemy(query_class=Query)
except OperationalError as e:
    time.sleep(5)
    db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True

    create_time = Column('create_time', Integer)
    delete_status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != id:
                setattr(self, key, value)

    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None
