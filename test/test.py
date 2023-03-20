"""
coding:utf-8
@Software : PyCharm
@File : test.py
@Time : 2023/3/16 11:41
@Author : Ryan Gao
@Email : 
@description : 
"""
from contextlib import contextmanager


class MyResource(object):
    def query(self):
        print('query data')


@contextmanager
def make_myresource():
    print('connect to resource')
    yield MyResource()
    print('close resource connect')


with make_myresource() as r:
    r.query()
