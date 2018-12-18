#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#post发送demo
import requests;
r=requests.post("http://localhost:8080/govCreditManage/indexImageNews/toDetail",
                headers={"Cookie":"JSESSIONID=810CE019211A55B66B5119556CAE7767"},
                data={"id":"1539829166556"});
print(r.status_code)
print(r.text)
#Todo 发送json
url="";
params = {'key': 'value'}
r_json = requests.post(url, json=params) # 内部自动序列化为JSON
#Todo 发送文件
upload_files = {'file': open('report.xls', 'rb')}
r_file = requests.post(url, files=upload_files)
#把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。