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


@web_blueprint.route('/')
def index():
    pass


@web_blueprint.route('/personal')
def personal_center():
    pass
