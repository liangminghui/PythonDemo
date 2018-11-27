#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# list = range(101)
# sum = 0
# for i in list:
#     sum = sum + i
#     print("hello%i" % i)
# print(sum);
ageList = ["18", "16", "18", "16", "18", "16", "16", "18", "18", "18", "16"]
for i in ageList:
    numI = int(i)
    if numI<18:
        print("有未成年,年龄%d"%numI)
        break;
index= 0
for i in ageList:
    index=index+1
    numI = int(i)
    if numI<18:
        print("第%i行有未成年,年龄%d"%(index,numI));
        continue;
