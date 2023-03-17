"""
coding:utf-8
@Software : PyCharm
@File : __init__.py.py
@Time : 2023/3/16 11:38
@Author : Ryan Gao
@Email :
@description : 
"""
from flask import Blueprint

# 创建蓝图
web_blueprint = Blueprint('web', __name__)

# 导入视图函数文件
from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
