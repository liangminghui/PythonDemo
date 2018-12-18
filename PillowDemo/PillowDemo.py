#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image,ImageFilter
im = Image.open("test.jpg")
w,h=im.size
print("图片的宽度和高度分别为%s,%s"%(w,h))
#缩放
im.thumbnail((w/2,h/2));
#im.save("test1_2.jpg","jpeg");
w,h=im.size
print(w,h)
im.filter(ImageFilter.BLUR);
#暂不保存
im.save("demo1_filter.jpg","jpeg");

