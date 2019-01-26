#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from util.common import log
# 百度网盘相关功能
log = log.LoggerUtil()


# 解析分享的url
def parse_url(share_url):
    share_url_list = re.findall('链接: (.*)? 复制', share_url)
    log.info("解析到%d条数据,内容如下>>>>"%(share_url_list.__len__()))
    for share_url_index in share_url_list:
        log.info(share_url_index)
    return share_url_list


# 保存分析的url
def save_url(single_share_url):
    # 截取出路径和提取码
    url, key = single_share_url.split(" 提取码: ")

    pass

save_url("https://pan.baidu.com/s/19UuXX-Q81NWdhMZ8Za2HGw 提取码: hwjd")

