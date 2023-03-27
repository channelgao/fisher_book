"""
coding:utf-8
@Software : PyCharm
@File : yushu.py
@Time : 2023/3/16 11:39
@Author : Ryan Gao
@Email :
@description : 
"""
from app import create_app

app = create_app(create_db=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=app.config.get('DEBUG', 'Ture'))
