__author__ = 'zhangxun'
#coding:utf-8

from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from datetime import datetime
from flask import render_template
from flask.ext.script import Manager
from flask.ext.script import Shell
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask import session
from flask import url_for
from flask import flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand

import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

#为了实现CSRF保护，为表单设置密钥
app.config['SECRET_KEY'] = 'hard to guess string'
#设置SQLALCHEMY的参数
app.config['SQLALCHEMY_DATABASE_URI']=\
    'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db=SQLAlchemy(app)
migrate=Migrate(app,db)

#增加命令行指令，初始化数据库，创建数据库模型，创建迁移仓库
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

#设置model
class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    users=db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True,index=True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


#name表单，代码中中文使用unicode
class NameForm(Form):
    name =StringField(u'你叫什么名字？', validators=[Required()])
    submit = SubmitField(u'提交')

#返回一个浏览器头部信息
# @app.route('/')
# def index():
#     user_agent = request.headers.get('User_Agent')
#     return '<p>Your browser is %s</p>' % user_agent

#自定义一个reponse
# @app.route('/')
# def index():
#     response = make_response('<h1>This document carries a cookies</h1>')
#     response.set_cookie('answer', '42')
#     return response

#跳转到其他网址
# @app.route('/')
# def index():
#     return redirect('http://www.baidu.com')

#使用表单
# @app.route('/', methods=['GET','POST'])
# def index():
# #    session.pop('_flashes', None)     flash中不能直接使用中文，必须前面加上u转成unicode
# #由于flash同样会产生session，所以产生一次unicodedecodeerror后会一指产生，所以可以用上述语句先清除掉
#     form=NameForm()
#     if form.validate_on_submit():
#         old_name=session.get('name')
#         if old_name is not None and old_name!=form.name.data:
#             flash(u'看起来你似乎改了名字！')
#         session['name']=form.name.data
#         return redirect(url_for('index'))
#     return render_template('index.html',
#                            form=form, name=session.get('name'))

#在视图中操作数据库
@app.route('/', methods=['GET','POST'])
def index():
#使用query查询数据库
    form=NameForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.name.data).first()
        if user is None:
            user=User(username=form.name.data)
            db.session.add(user)
            session['known']=False
        else:
            session['known']=True
        session['name']=form.name.data
        form.name.data=''
        return redirect(url_for('index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known',False))

# #响应url地址的参数
# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s!</h1>' % name

#使用模板
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

#自定义错误页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
#    app.run(debug=True)
    manager.run()