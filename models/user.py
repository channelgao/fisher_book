"""
coding:utf-8
@Software : PyCharm
@File : user.py
@Time : 2023/3/17 17:02
@Author : Ryan Gao
@Email : 
@description : 
"""
from sqlalchemy import Integer, String, Column, Boolean, Float

from base import Base


class User(Base):
    __tablename__ = 'user'
    # __bind_key__ = 'fisher'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))
