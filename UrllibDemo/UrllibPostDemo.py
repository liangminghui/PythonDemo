#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# urllib案例发送post请求
# data以bytes形式传入
from urllib import request, parse;

print("<<<start");
login_data = parse.urlencode([
    ("name", ""),
]);
req = request.Request("//自己的网站需要啥就用啥");
req.add_header("Cookie","JSESSIONID=FF49D88A4551251898DB65CB5AF2DB63");
with request.urlopen(req,data=login_data.encode("utf-8")) as f:
    print("State",f.status,f.reason);
    for k,v in f.getheaders():
        print("%s%s"%(k,v));
    print(f.read().decode("utf-8"));
print("end>>>>>");

