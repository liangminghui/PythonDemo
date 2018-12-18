#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image
im = Image.open("demo.png")
w,h=im.size
print("图片的宽度和高度分别为%s,%s"%(w,h))