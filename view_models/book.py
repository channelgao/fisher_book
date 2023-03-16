"""
coding:utf-8
@Software : PyCharm
@File : book.py
@Time : 2023/3/16 11:41
@Author : Ryan Gao
@Email : 
@description : 
"""


class BookViewModel(object):
    """
    处理 book spider 赋值完成的成员变量 （单个book数据）
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
    处理 book
    """

    def __init__(self, book):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, books_object, keyword):
        self.total = books_object.total
        self.books = [BookViewModel() for book in books_object.books]
        self.keyword = keyword
