"""
coding:utf-8
@Software : PyCharm
@File :
@Time : 2023/3/16 11:39
@Author : Ryan Gao
@Email :
@description :
"""
from flask import current_app, flash, redirect, url_for
from flask_login import login_required, current_user

from models.base import db
from models.gift import Gift
from . import web_blueprint


@web_blueprint.route('/my/gifts')
@login_required
def my_gifts():
    return 'my gifts'


@web_blueprint.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            # 实例化礼物model对象
            gift = Gift()
            gift.isbn = isbn
            # current_user 为当前用户
            gift.uid = current_user.id
            # 书籍添加成功即增加用户beans
            current_user.beans += current_app.config.get('BEANS_UPLOAD_ONE_BOOK')
            db.session.add(gift)
        flash('书籍赠送成功！')
    else:
        flash('这本书已存在于您的愿望清单里，或您已赠送此书请不要重复添加！')

    return redirect(url_for('web.book_detail', isbn=isbn))


@web_blueprint.route('/gifts/<gid>/redraw')
@login_required
def redraw_from_gifts(gid):
    pass
