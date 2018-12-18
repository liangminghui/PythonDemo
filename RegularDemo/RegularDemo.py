#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#正则表达式使用
import re;
# print(re.match("00\d","001"));
#如果匹配成功，返回一个Match对象，否则返回None
a=input("请输入邮箱");
print(a);
if re.match("\d{5,12}@\w+",a):
    print("格式正确>>>");
else:
    print("格式有误>>>");