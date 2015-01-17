__author__ = 'zhangxun'
#coding:utf-8

from flask import render_template, session, redirect, url_for
from .forms import NameForm
from ..models import User
from .. import db

from . import main

#在视图中操作数据库
@main.route('/', methods=['GET','POST'])
def index():
#使用query查询数据库
    form=NameForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.name.data).first()
        if user is None:
            user=User(username=form.name.data)
            db.session.add(user)
            session['known']=False
            #每当表单接收到新名字时，向管理员发送邮件
            # if app.config['FLASKY_ADMIN']:
            #     send_email(app.config['FLASKY_ADMIN'],'New User',
            #                'mail/new_user',user=user)
        else:
            session['known']=True
        session['name']=form.name.data
        form.name.data=''
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known',False))