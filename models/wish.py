"""
coding:utf-8
@Software : PyCharm
@File : wish.py
@Time : 2023/3/20 8:31
@Author : Ryan Gao
@Email : 
@description : 
"""
from sqlalchemy import Integer, Column, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship

from models.base import Base


class Wish(Base):
    __tablename__ = 'wish'

    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)
