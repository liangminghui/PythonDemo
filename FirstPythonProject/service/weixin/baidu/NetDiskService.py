#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# service层
from util.baidu import NetDisk
from constant import Result


def save_url(param):

    NetDisk.parse_url(param)
    result = Result.JsonResult("200", "调用成功", True)
    return result


