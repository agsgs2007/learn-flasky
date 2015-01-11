__author__ = 'zhangxun'
#coding:utf-8

from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import render_template

app = Flask(__name__)

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

#使用模板
@app.route('/')
def index():
    return render_template('index.html')

# #响应url地址的参数
# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s!</h1>' % name

#使用模板
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)