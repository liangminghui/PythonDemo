#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 测试类
# 参考地址 https://github.com/hanandjun/weifangbus/blob/develop/lib/utils/requestParamsUtil.dart
import time
import random


def run():
    print(">>>")


# 获取时间戳
def _get_time_stamp():
    str_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    return str_time


# 获取随机数 100-1000
def _get_random():
    return random.randint(100, 1000)


# 生成签名密钥
def _get_sign_key(time_stamp, rand):
    print(time_stamp)
    print(rand)


if __name__ == '__main__':
    time_stamp = _get_time_stamp()
    rand = _get_random()
    _get_sign_key(_get_random())

