#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 用于生成日报


class MyExcel(object):
    def __init__(self, content, hours ,finish_percent , not_finish_reason ):
        self.content = content
        self.hours = hours
        self.finish_percent = finish_percent
        self.not_finish_reason = not_finish_reason


# 写入excel文件
def write_excel():
    root_path = "D:\workspace\eclipse\网站组\公共\工作情况\周报"
    with open("../resources/template.xlsx","rb") as f:
        with open("../resources/template1.xlsx","wb") as f2:
            f2.write(f.read())
            f2.close()
        f.close()


# 向excel文件写入数据
def write_data_to_excel(excel_object):
    pass


if __name__=="__main__":
    write_excel()




