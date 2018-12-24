#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 基于mvc实现登录验证
# 使用的是jinja2
from flask import Flask, request, render_template
import SqlDemo

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def index():
    return render_template("index.html")


@app.route('/toLogin', methods=['get'])
def toLogin():
    return render_template("login.html")


@app.route('/login', methods=['post'])
def login():
    username = request.form['username']
    password = request.form['password']
    result,msg = SqlDemo.login(username, password)
    if result:
        return render_template('success.html', username=username, books=SqlDemo.getUsersBookInfo(msg.id))
    else:
        return render_template('login.html', message=msg, username=username)


if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)
