#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 图片识别demo，使用百度AI，需先创建对应的图像识别应用
# 通用文字识别
import requests
import json
client_api_key = "Q72wx1qOCL8pYxtCnEQ2wuFt"
client_secret_key = "Xh981XBDdgGkqGH3DjuxagjQuQuUFV7H"
general_basic_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
def getAccessToken():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+client_api_key+'&client_secret='+client_secret_key
    headers = {
        'Content-Type': 'application/json; charset=UTF-8'
    }
    result = requests.get(host,headers=headers)
    result = json.loads(result.text)
    return result["access_token"]
#https://blog.csdn.net/u013421629/article/details/79500336
print(getAccessToken())