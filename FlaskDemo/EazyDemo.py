#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 简单的flask   demo
# 需要先执行pip install flask
#非mvc形式，html由后端编写好
from flask import Flask,request
import SqlDemo
app = Flask(__name__)
app.config.update(DEBUG=True)


@app.route("/", methods=['GET', 'POST'])
def home():
    return '<h1>Home11</home>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
                    <p><input name="username"/></p>
                    <p><input name="password" type="password"/></p>
                    <p><button type="submit">Sign In</button></p>
                    </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # request获取表单内容
    # if request.form['username'] == 'admin' and request.form['password'] == 'password':
    #     return '<h3>Hello admin</h3>'
    # return '<h3>用户不存在或密码错误</h3>'
    result,msg=SqlDemo.login(request.form['username'],request.form['password'])
    if result:
        #读取用户对应书的信息
        books=SqlDemo.getUsersBookInfo(msg.id)
        bookInfo=""
        for book in books:
            bookInfo= bookInfo+"《%s》<br/>"%book.name
        return '<h3>Hello %s,您的藏书目录如下</h3>%s'%(msg.name,bookInfo)
    else:
        return '<h3>登陆失败:%s</h3>'%msg


if __name__ == '__main__':
    app.run('127.0.0.1',5000,debug=True)
