"""
coding:utf-8
@Software : PyCharm
@File :
@Time : 2023/3/16 11:39
@Author : Ryan Gao
@Email :
@description :
"""
from . import web_blueprint


@web_blueprint.route('/my/wish')
def my_wish():
    pass


@web_blueprint.route('/wish/book/<isbn>')
def save_to_wish(isbn):
    pass


@web_blueprint.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web_blueprint.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
