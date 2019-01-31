#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 漫画项目
from flask import Flask,render_template,jsonify,request
import json
from demo.manhua.common import log
log = log.LoggerUtil()
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index_url():
    return render_template("index.html")


@app.route("/ajaxLoad", methods=["POST"])
def ajaxLoad():
    data = json.loads(request.get_data())
    index = data['index']
    if index is None:
        message = "index未传入"
        code = 400
    else:
        message = index
        if index == '1':
            code = 200
        elif index == '2':
            code = 200
        elif index == '3':
            code = 200
        elif index == '4':
            code = 200
        else:
            code = 500
            message = "不支持的index"+message

    result_data = {
        'code': code,
        'msg': message,
        'data': index
    }
    log.info(result_data)
    return jsonify(result_data)



if __name__=='__main__':
    app.run('127.0.0.1', 5000, debug=True)


