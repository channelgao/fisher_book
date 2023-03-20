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
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from libs.isbn_selector import is_isbn
from models.base import Base
from models.gift import Gift
from models.wish import Wish
from spider.book_spider import BookSpider


class User(UserMixin, Base):
    __tablename__ = 'user'
    # __bind_key__ = 'fisher'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    _password = Column('password', String(128), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def can_save_to_list(self, isbn):
        # 判断是否为ISBN编号
        if not is_isbn(isbn):
            return False

        # 实例化书籍spider
        book_spider = BookSpider()
        book_spider.search_by_isbn(isbn)
        if not book_spider.get_first_book:
            return False

        # 禁止用户同时赠送多本相同图书
        # 一个用户不能同时成为赠送者和索要者
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        # 既不在心愿清单也不在赠送清单里即可添加
        if gifting or wishing:
            return False
        else:
            return True

