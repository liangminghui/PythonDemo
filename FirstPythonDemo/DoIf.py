# -*- coding: utf-8 -*-
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
height = 1.75
weight = 80.5
r = float("%.2f" % (weight / (height * height)))
if r <= 18.5:
    res = "过轻"
elif 18.5 < r <= 25:
    res = "正常"
elif 25 < r <= 28:
    res = "过重"
elif 28 < r <= 32:
    res = "肥胖"
elif r>32:
    res = "严重肥胖"
print("小明体重参数为%.2f情况为%s"%(r,res))

