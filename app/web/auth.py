"""
coding:utf-8
@Software : PyCharm
@File :
@Time : 2023/3/16 11:39
@Author : Ryan Gao
@Email :
@description :
"""
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user

from . import web_blueprint
from forms.auth import RegisterForm, LoginForm
from models.user import User
from models.base import db


@web_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            next_url = request.args.get('next')
            # 避免重定向攻击
            if not next_url or not next_url.startswith('/'):
                next_url = url_for('web.index')
            return redirect(next_url)
        else:
            flash('账号不存在或者密码错误！')
    return render_template('auth/login.html', form=form)


@web_blueprint.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web_blueprint.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web_blueprint.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web_blueprint.route('/logout')
def logout():
    pass
