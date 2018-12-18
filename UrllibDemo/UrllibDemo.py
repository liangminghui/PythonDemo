#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#简单的urllib案例
from urllib import request;
with request.urlopen("https://api.douban.com/v2/book/2129650") as f:
    data=f.read()
    print("State",f.status,f.reason)
    for k,v in f.getheaders():
        print('%s%s'%(k,v));
    print("date",data.decode("utf-8"))