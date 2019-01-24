#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 统一返回结果类 code(404之类), msg(信息), dictionary(key-value键值对), data(封装数据)
import json


class JsonResult(object):
    def __init__(self, code, msg, flag, dictionary, data):
        self.code = code
        self.msg = msg
        self.flag = flag
        self.dictionary = dictionary
        self.data = data

    def __init__(self, code, msg, flag):
        self.code = code
        self.msg = msg
        self.flag = flag


def obj_2_json_simple(obj):
    return {
        "code": obj.code,
        "msg": obj.msg
    }


def obj_2_json_with_data(obj):
    return {
        "code": obj.code,
        "msg": obj.msg,
        "data": obj.data
    }


def obj_2_json(obj):
    return json.dumps(obj, default=obj_2_json_simple,ensure_ascii=False)




