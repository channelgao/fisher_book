"""
coding:utf-8
@Software : PyCharm
@File : httper.py
@Time : 2023/3/16 11:40
@Author : Ryan Gao
@Email :
@description : 
"""
import requests


class HTTP(object):
    
    @staticmethod
    def get(url, return_json=True):
        # requests 发送 get 请求
        get_response = requests.get(url)
        # api 返回状态码非200
        if get_response.status_code != 200:
            return {} if return_json else ''
        # 正常返回
        return get_response.json() if return_json else get_response.text
