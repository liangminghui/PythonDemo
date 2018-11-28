# -*- coding: utf-8 -*-
# print('%.2f' % 3.1415926)
# print('%02d.%02d' % (3, 1))
# print('%.2f' % 3.1415926)
# s1 = int(72);
# s2 = int(85);
# r = float(85-72)/72;
# print("小明成绩提高百分之%.4f"%r)
# from OnePlaceQuadratic import quadratic
# from OnePlaceQuadratic import my_function
# x,y=
# print(quadratic(1,3,-4))
# print(my_function(5,6,7))
# 判断是否可以迭代
from collections import Iterable

# isinstance('abc', Iterable)
#
# print(isinstance('abc', Iterable))
#
#
def findMinAndMax(list):
    if list.__len__() == 0:
        return None, None
    elif list.__len__() == 1:
        return list[0], list[0]
    else:
        max = list[0]
        min = list[0]
        for index in list:
            if index > max:
                max = index
            if index < min:
                min = index
        return min, max
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print(findMinAndMax([7, 1]))
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[x.lower() for x in L1 if isinstance(x, str) == True]
# 测试:
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
