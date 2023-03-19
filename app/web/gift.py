"""
coding:utf-8
@Software : PyCharm
@File :
@Time : 2023/3/16 11:39
@Author : Ryan Gao
@Email :
@description :
"""
from flask_login import login_required

from . import web_blueprint


@web_blueprint.route('/my/gifts')
@login_required
def my_gifts():
    return 'my gifts'


@web_blueprint.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    pass


@web_blueprint.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
