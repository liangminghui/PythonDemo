#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pip install chardet
# 检测编码
import chardet;
byteStr=b'abc';
#print(chardet.detect(byteStr));
gbkStr="离离原上草，一岁一枯荣".encode("gbk")
#print(chardet.detect(gbkStr));
utf8Str="离离原上草，一岁一枯荣".encode("utf-8")
#print(chardet.detect(utf8Str));
japanStr="最新の主要ニュース".encode("euc-jp");
print(chardet.detect(japanStr));



