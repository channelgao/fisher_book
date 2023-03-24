"""
coding:utf-8
@Software : PyCharm
@File : gift.py
@Time : 2023/3/17 17:02
@Author : Ryan Gao
@Email : 
@description : 
"""
from flask import current_app
from sqlalchemy import Integer, Column, Boolean, ForeignKey, String, desc
from sqlalchemy.orm import relationship

from models.base import Base
from spider.book_spider import BookSpider


class Gift(Base):
    __tablename__ = 'gift'

    id = Column(Integer, primary_key=True)
    # 用户信息，和下方uid绑定，只需赋值uid，读取时使用user
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @property
    def get_book(self):
        book_spider = BookSpider()
        book_spider.search_by_isbn(self.isbn)
        return book_spider.get_first_book

    # 类方法放在类中，可以返回多条记录，成员方法不合适
    @classmethod
    def recent(cls):
        recent_gifts = Gift.query.filter_by(launched=False).group_by(Gift.isbn).order_by(desc(Gift.create_time)).limit(
            current_app.config.get('RECENT_BOOK_COUNT')).distinct().all()
        return recent_gifts
