"""
coding:utf-8
@Software : PyCharm
@File :
@Time : 2023/3/16 11:39
@Author : Ryan Gao
@Email :
@description :
"""
from flask import render_template

from models.book import Book
from models.gift import Gift
from view_models.book import BookViewModel
from . import web_blueprint


@web_blueprint.route('/')
def index():
    recent_gifts = Gift.recent()
    books = [BookViewModel(gift.book) for gift in recent_gifts]
    return render_template('index.html', recent=books)


@web_blueprint.route('/personal')
def personal_center():
    pass
