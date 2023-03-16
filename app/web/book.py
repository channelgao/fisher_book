"""
coding:utf-8
@Software : PyCharm
@File : book.py
@Time : 2023/3/16 11:39
@Author : Ryan Gao
@Email :
@description : 
"""
from flask import request

from . import web_blueprint
from forms.book import SearchForm
from spider.book_spider import BookSpider


@web_blueprint.route('/')
def hello():
    return 'hello flask!'


@web_blueprint.route('/book/search')
def search():
    # 引入 forms 验证 用户的输入数据
    form = SearchForm(request.args)
    # 读取清洗后的数据
    q = form.q.data
    page = form.page.data
    # 判断 is_isbn_or_key 的值
    is_isbn_or_key = True
    if is_isbn_or_key:
        # 使用 isbn api 获取数据
        pass

    else:
        # 使用 关键字 api 获取数据
        pass


