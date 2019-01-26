#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 图片识别demo，使用百度AI，需先创建对应的图像识别应用
# 通用文字识别
import requests
import json
import base64
client_api_key = "Q72wx1qOCL8pYxtCnEQ2wuFt"
client_secret_key = "Xh981XBDdgGkqGH3DjuxagjQuQuUFV7H"
accurate_basic_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
def getAccessToken():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+client_api_key+'&client_secret='+client_secret_key
    headers = {
        'Content-Type': 'application/json; charset=UTF-8'
    }
    result = requests.get(host,headers=headers)
    result = json.loads(result.text)
    return result["access_token"]
def AIPhotoWordShiBie():
    access_token = getAccessToken()
    headers = {
        'Content-Type':'application/x-www-form-urlencoded'
    }
    with open("6273713-969204f566394e4c.jpg", "rb") as f:
        image = base64.b64encode(f.read())
    body = {
        'image':image
    }
    result = requests.post(accurate_basic_url+"?access_token="+access_token,headers=headers,data=body)
    words_result = json.loads(result.text)["words_result"]
    for words in words_result:
        print(words["words"])

if __name__ == '__main__':
    AIPhotoWordShiBie()
