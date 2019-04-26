#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 测试类
# 参考地址 https://github.com/hanandjun/weifangbus/blob/develop/lib/utils/requestParamsUtil.dart
import time
import random
import hashlib
import hmac
import base64

# 59485eebe12042cba33e972f77834b6b 聊城
# 55b73c446e914785862966abf9a29416 潍坊
app_key = "55b73c446e914785862966abf9a29416"


# 获取时间戳
def _get_time_stamp():
    str_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    return str_time


# 获取随机数 100-1000
def _get_random():
    return random.randint(100, 1000)


# 生成签名密钥
def _get_sign_key(time_stamp, rand):
    message = bytes(str(time_stamp) + str(rand), encoding="utf-8")
    secret = bytes(app_key, "utf-8")
    signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())
    print(signature)


if __name__ == '__main__':
    time_stamp = _get_time_stamp()
    rand = _get_random()
    _get_sign_key(time_stamp, rand)
