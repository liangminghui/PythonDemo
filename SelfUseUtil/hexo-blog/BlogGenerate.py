#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 博客生成器,使适用于HEXO博客
# 爬取CSDN的博客内容，生成HEXO的文件
import requests
from lxml import etree


def read_csdn_blog_info(csdn_url: str):
    result_text = requests.get(csdn_url).text
    result_html = etree.HTML(result_text)
    result_message = result_html.xpath("//div[@id = 'content_views']/p/text()")
    for message in result_message:
        if message is not None:
            print(message)
    result_message = result_html.xpath("//div[@id = 'content_views']/p/img/@src")
    for message in result_message:
        if message is not None:
            print(message)


if __name__ == '__main__':
    read_csdn_blog_info("https://blog.csdn.net/qq_36264455/article/details/79934825")

