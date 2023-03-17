"""
coding:utf-8
@Software : PyCharm
@File : __init__.py
@Time : 2023/3/17 13:24
@Author : Ryan Gao
@Email : 
@description : 
"""
from flask import Blueprint

# 创建蓝图
download_blueprint = Blueprint('download', __name__, static_folder='recipe_files')

# 导入视图函数文件
from app.recipe import download