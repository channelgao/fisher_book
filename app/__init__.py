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
from flask_login import LoginManager

from app.web import web_blueprint
from app.recipe import download_blueprint
from models.base import db

login_manager = LoginManager()


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
    # 初始化 login_manager
    login_manager.init_app(app)
    # 登录页面的视图函数
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请您先登录，再进行后续操作'
    # 数据库中新建数据表
    if create_db:
        with app.app_context():
            db.create_all()

    return app


def register_blueprint(app):
    app.register_blueprint(web_blueprint, url_prefix='/book')
    app.register_blueprint(download_blueprint, url_prefix='/recipe')


@login_manager.user_loader
def load_user(user_id):
    # 用户加载函数
    from models.user import User
    user = db.session.query(User).get(user_id)
    return user
