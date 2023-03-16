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
web_blueprint = Blueprint('web_blueprint', __name__)

# 导入视图函数文件
from app.web import book