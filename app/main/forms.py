__author__ = 'zhangxun'
#coding:utf-8

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

#name表单，代码中中文使用unicode
class NameForm(Form):
    name =StringField(u'你叫什么名字？', validators=[Required()])
    submit = SubmitField(u'提交')
