"""
coding:utf-8
@Software : PyCharm
@File : gift.py
@Time : 2023/3/17 17:02
@Author : Ryan Gao
@Email : 
@description : 
"""
from sqlalchemy import Integer, Column, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship

from models.base import Base


class Gift(Base):
    __tablename__ = 'gift'

    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)
