"""
@coding: utf-8
@software: PyCharm
@Name: auth.py
@Auth: Ryan Gao
@Email:
@Date: 2023/3/17 19:55
@Desc: 
"""
from wtforms import Form, StringField, PasswordField
from wtforms.validators import length, DataRequired, Email, ValidationError

from models.user import User


class RegisterForm(Form):
    nickname = StringField(validators=[DataRequired(), length(2, 16, message='昵称至少2各字符，最多16个字符！')])
    email = StringField(validators=[DataRequired(), length(8, 64), Email(message='电子邮箱格式不正确！')])
    password = PasswordField(validators=[DataRequired(message='密码不能为空！'), length(6, 32)])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册！')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已被注册！')


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), length(2, 16, message='昵称至少2各字符，最多16个字符！')])
    password = PasswordField(validators=[DataRequired(message='密码不能为空！'), length(6, 32)])
