#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 测试爬虫
import requests
from lxml import etree
import sqlite3
from demo.manhua.common import log
log = log.LoggerUtil()


def get_connect():
    return sqlite3.connect("database.db")


def close_connect(cursor, connect):
    cursor.close()
    connect.commit()
    connect.close()


def read_html():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'panel=1; Hm_lvt_b45154d16998acbff1cc0ef16659fd1d=1548904268,1548906115,1548912747; Hm_lpvt_b45154d16998acbff1cc0ef16659fd1d=1548912758'
                  'Host: m.pufei.net',
        'Pragma': 'no-cache',
        'Referer': 'http://m.pufei.net/manhua/320/24550.html',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }
    result = requests.get("http://m.pufei.net/manhua/320/", headers=headers)
    result.encoding = 'gb2312'
    html = etree.HTML(result.text)
    html_a_list = html.xpath('//div/ul/li/a')
    for info in html_a_list:
        if not info.xpath('@title') == []:
            save_to_db(info.xpath('@href')[0], info.xpath('@title')[0])


def save_to_db(href, title):
    connect = get_connect()
    cursor = connect.cursor()
    href_result = cursor.execute("select href,title from comic_info where href = '%s' " % href).fetchone()
    if href_result is None:
        cursor.execute('''insert into comic_info (href,title) values ('%s','%s')''' % (href, title))
    close_connect(cursor, connect)


def create_db_table():
    connect = get_connect()
    cursor = connect.cursor()
    try:
        cursor.execute(
            '''CREATE TABLE comic_info(
                id INTEGER primary key AUTOINCREMENT,
                title varchar(100) ,
                href varchar(100))''')
        message = '表格创建完成'
    except sqlite3.OperationalError as e:
        message = '表格已存在'
    finally:
        print(message)
        close_connect(cursor,connect)


def query_comic_info():
    connect = get_connect()
    cursor = connect.cursor()
    print(cursor.execute('''select * from comic_info''').fetchall())
    close_connect(cursor, connect)


def tong_bu():
    print('开始同步信息', '>'*10)
    create_db_table()
    read_html()
    print('同步信息结束', '<'*10)
    log.info('同步了一次信息')


if __name__ == '__main__':
    #tong_bu()
    query_comic_info()



