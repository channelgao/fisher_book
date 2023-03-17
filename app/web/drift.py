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


@web_blueprint.route('/drift/<int:gid>', methods=['GET', 'POST'])
def send_drift(gid):
    pass


@web_blueprint.route('/pending')
def pending():
    pass


@web_blueprint.route('/drift/<int:did>/reject')
def reject_drift(did):
    pass


@web_blueprint.route('/drift/<int:did>/redraw')
def redraw_drift(did):
    pass


@web_blueprint.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    pass
