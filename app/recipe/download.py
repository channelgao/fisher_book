"""
coding:utf-8
@Software : PyCharm
@File : download.py
@Time : 2023/3/17 13:25
@Author : Ryan Gao
@Email : 
@description : 
"""
from flask import request

from . import download_blueprint


@download_blueprint.route('/test')
def recipe_test():
    return 'hello recipe test!'


@download_blueprint.route('/download')
def recipe_download():
    # 配方下载权限控制
    has_authorization = False
    if has_authorization:
        # 获取需要下载的配方名
        recipe = request.args.get('recipe')
        # 返回配方文件
        file = download_blueprint.send_static_file(recipe)
        return file
    else:
        return 'no authorization!'
