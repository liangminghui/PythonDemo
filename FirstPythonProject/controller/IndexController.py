#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 没有找到Controller分开的方法，暂时使用单Controller启动
from flask import Flask,request
from service.weixin.baidu import NetDiskService
import json
from constant import Result
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return '''
            <h1>首页<hi>
            <form action="getParam" method="post">
                <p><textarea name="param"></textarea></p>
                <p><button type="submit">发送</button></p>
            </form>'''


@app.route('/getParam', methods=['POST'])
def get_param():
    return Result.obj_2_json(NetDiskService.save_url(request.form["param"]))


if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)
