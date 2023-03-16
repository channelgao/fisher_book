"""
coding:utf-8
@Software : PyCharm
@File : __init__.py.py
@Time : 2023/3/16 11:38
@Author : Ryan Gao
@Email :
@description : 
"""
from flask import Flask

from app.web import web_blueprint
from models.book import db


def create_app(create_db=False):
    # 实例化 flask app
    app = Flask(__name__)
    # 从对象导入配置文件
    app.config.from_object('config.secure')
    app.config.from_object('config.setting')
    # 蓝图注册
    register_blueprint(app)
    # 数据库注册
    db.init_app(app)
    # 数据库中新建数据表
    if create_db:
        with app.app_context():
            db.create_all()

    return app


def register_blueprint(app):
    app.register_blueprint(web_blueprint, url_prefix='/')
