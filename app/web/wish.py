"""
coding:utf-8
@Software : PyCharm
@File :
@Time : 2023/3/16 11:39
@Author : Ryan Gao
@Email :
@description :
"""
from flask import flash, current_app, redirect, url_for
from flask_login import login_required, current_user

from models.base import db
from models.wish import Wish
from . import web_blueprint


@web_blueprint.route('/my/wish')
def my_wish():
    pass


@web_blueprint.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            # 实例化礼物model对象
            wish = Wish()
            wish.isbn = isbn
            # current_user 为当前用户
            wish.uid = current_user.id
            db.session.add(wish)
        flash('书籍添加成功！')
    else:
        flash('这本书已存在于您的愿望清单里，或您已赠送此书请不要重复添加！')

    return redirect(url_for('web.book_detail', isbn=isbn))


@web_blueprint.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web_blueprint.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
