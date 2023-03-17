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


@web_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    pass


@web_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    pass


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
