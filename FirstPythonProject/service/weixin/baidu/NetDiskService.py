#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# service层
from util.baidu import NetDisk
from constant import Result


def save_url(param):

    share_url_list = NetDisk.parse_url(param)
    if share_url_list.__len__() == 0:
        result = Result.JsonResult("200", "解析出0条数据", True)
        return result
    for url in share_url_list:
        NetDisk.save_url(url)
    result = Result.JsonResult("200", "调用成功", True)
    return result




