"""
coding:utf-8
@Software : PyCharm
@File : book_spider.py
@Time : 2023/3/16 11:40
@Author : Ryan Gao
@Email :
@description : 
"""
from libs.httper import HTTP


class BookSpider(object):
    # 三方 API 链接
    isbn_url = 'http://t.talelin.com/v2/book/isbn/{}'
    keyword_url = 'http://t.talelin.com/v2/book/search?q={}&page={}'

    def __init__(self):
        # 初始化书籍总量、书籍列表
        self.total = 0
        # 不同接口保持相同类型输出，保证接口输出格式的一致性，便于前端解析
        self.books = []

    def __fill_single(self, data):
        # isbn 接口获取数据，将 data 全部保存至 self.books
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        # 关键字接口获取数据，将 data 全部保存至 self.books
        if data:
            self.total = data.get('total')
            self.books = data.get('books')

    def search_by_isbn(self, isbn):
        # 通过 isbn 获取书籍数据
        url = self.isbn_url.format(isbn)
        get_response = HTTP.get(url, return_json=True)
        if len(get_response) > 0:
            # http返回 包含数据
            # 可以添加数据库验证保存提取
            self.__fill_single(get_response)

    def search_by_keyword(self, keyword, page):
        # 通过 keyword 获取书籍数据
        url = self.keyword_url.format(keyword, page)
        get_response = HTTP.get(url, return_json=True)
        if len(get_response) > 0:
            # http返回 包含数据
            # 可以添加数据库验证保存提取
            self.__fill_collection(get_response)

    @property
    def get_first_book(self):
        return self.books[0] if self.total >= 1 else None
