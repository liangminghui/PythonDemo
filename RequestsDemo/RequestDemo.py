#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#比urllib更简单，先执行pip install requests
import requests;
r=requests.get("https://www.douban.com/");
print(r.status_code);
#print(r.text)
print(r.headers)
# r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
# print(r.url)
# print(r.encoding)
# #print(r.content)
# print(r.text)
# r_json = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r_json.json())
# 获取头部header信息
print(r.headers['Content-Type'])
#cookie
url="";
cs = {'token': '12345', 'status': 'working'}
r = requests.get(url, cookies=cs)
#超时
r = requests.get(url, timeout=2.5) # 2.5秒后超时