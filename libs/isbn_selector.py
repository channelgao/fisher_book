"""
coding:utf-8
@Software : PyCharm
@File : isbn_selector.py
@Time : 2023/3/17 15:28
@Author : Ryan Gao
@Email : 
@description : 
"""


def is_isbn(word):
    """
    判断word是否为isbn
    :param word:
    :return:
    """
    # 默认当前word不为isbn，即False
    isbn_or_key = False
    if (len(word) == 13) and (word.isdigit()):
        isbn_or_key = True
    short_word = word.replace('-', '')
    if ('-' in word) and (len(short_word) == 10) and (short_word.isdigit()):
        isbn_or_key = True
    return isbn_or_key
