"""
coding:utf-8
@Software : PyCharm
@File : book.py
@Time : 2023/3/16 11:39
@Author : Ryan Gao
@Email :
@description : 
"""
import json
from flask import request, render_template, flash

from . import web_blueprint
from forms.book import SearchForm
from libs.isbn_selector import is_isbn
from spider.book_spider import BookSpider
from view_models.book import BookCollection, BookViewModel


@web_blueprint.route('/<isbn>/detail')
def book_detail(isbn):
    book_spider = BookSpider()
    book_spider.search_by_isbn(isbn)
    book_view_model = BookViewModel(book_spider.get_first_book)
    return render_template('book_detail.html', book=book_view_model, wishes=[], gifts=[])


@web_blueprint.route('/search')
def search():
    # 引入 forms 验证 用户的输入数据
    form = SearchForm(request.args)
    # 实例化数据格式转换
    book_collection = BookCollection()
    # 表单验证
    if form.validate():
        # 实例化书籍数据接入
        book_spider = BookSpider()

        # 读取清洗后的数据
        q = form.q.data
        page = form.page.data
        # 判断 is_isbn_or_key 的值
        is_isbn_or_key = is_isbn(q)

        if is_isbn_or_key:
            # 使用 isbn api 获取数据
            book_spider.search_by_isbn(isbn=q)
        else:
            # 使用 关键字 api 获取数据
            book_spider.search_by_keyword(keyword=q, page=page)

        # 书籍格式封装
        book_collection.fill(book_spider, q)
        # 存在成员为 object 的情况， 所以无法直接使用book_collection.__dict__的方式取出成员变量
        # return json.dumps(book_collection, default=lambda o: o.__dict__)

    else:
        flash('搜索的关键字不和要求！请重新输入！')
        # return jsonify(form.errors)

    return render_template('search_result.html', books=book_collection)
