#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Excel 读取
import xlrd


def read(file_path, sheet_index):
    try:
        data = xlrd.open_workbook(file_path)
        # 通过索引顺序获取
        sheet = data.sheets()[sheet_index]
        return sheet
    except FileNotFoundError as e:
        print("文件不存在", e)


