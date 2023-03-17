"""
coding:utf-8
@Software : PyCharm
@File : book.py
@Time : 2023/3/16 11:41
@Author : Ryan Gao
@Email : 
@description : 
"""
"""
    因为前端需要的数据和三方api返回的数据结构不一致，所以处理 book spider 赋值完成的成员变量 （单个book数据）
"""


class BookViewModel(object):
    """
    单本书籍的数据结构定义
    """

    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.pages = book['pages']
        self.author = book['author']
        self.price = book['price']
        self.summary = book['summary']
        self.image = book['image']


class BookCollection(object):
    """
    单本 & 多本书籍的返回前端的数据结构定义
    """

    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, spider_books_object, keyword):
        self.total = spider_books_object.total
        self.books = [BookViewModel(book) for book in spider_books_object.books]
        self.keyword = keyword
