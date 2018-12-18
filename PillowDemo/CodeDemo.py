#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#验证码Demo
from  PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
#随机字母
def randomChar():
    return chr(random.randint(65,90));

#随机颜色
def randomColor():
    return (random.randint(60,255),random.randint(60,255),random.randint(60,255));
def randomColor2():
    return (random.randint(30,127),random.randint(30,127),random.randint(30,127));
print(randomColor())
width=60*4;
height=60;
image=Image.new("RGB",(width,height),(255,255,255));
font=ImageFont.truetype("consola.ttf",36);
draw=ImageDraw.Draw(image);
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=randomColor());
for t in range(4):
    draw.text((60*t+10,10),randomChar(),font=font,fill=randomColor2());
#模糊处理
image=image.filter(ImageFilter.BLUR);
image.save("code.png","png");



