__author__ = 'zhangxun'
#coding:utf-8

from . import mail
from flask.ext.mail import Message
from flask import render_template, current_app

#异步发送邮件
from threading import Thread

def send_async_email(app,msg):
    with app.app_context():
        mail.send_message(msg)

def send_email(to, subject, template, **kwargs):
    app=current_app._get_current_object()
    msg=Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX']+subject,
                sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body=render_template(template+'.txt', **kwargs)
    msg.html=render_template(template+'.html', **kwargs)
    thr=Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
