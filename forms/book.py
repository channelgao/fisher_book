"""
coding:utf-8
@Software : PyCharm
@File : book.py
@Time : 2023/3/16 11:39
@Author : Ryan Gao
@Email :
@description : 
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[length(min=1, max=30), DataRequired()])
    page = IntegerField(validators=[NumberRange(min=1, max=99, message='页数需要大于1且小于99')], default=1)
