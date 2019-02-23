#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mysql connect
import pymysql


class MySqlConnect(object):
    def __init__(self, ip, username, password, database):
        self.ip = ip
        self.userName = username
        self.password = password
        self.database = database


def getConnect(mysql_connect):
    # mySqlConnect = MySqlConnect("192.168.1.251", "develop", "develop251", "website_yantai_develop")
    # 使用cursor()方法创建一个游标对象
    # 使用execute()方法执行SQL语句
    # fetchall()获取全部数据
    # 打印获取到的数据
    connect = pymysql.connect(mysql_connect.ip, mysql_connect.userName, mysql_connect.password, mysql_connect.database)
    cursor = connect.cursor()
    return connect, cursor


def closeConnect(cursor, connect):
    cursor.close()
    connect.close()


if __name__ == '__main__':
    mySqlConnect = MySqlConnect("192.168.1.251", "develop", "develop251", "website_yantai_develop")
    MySqlConnect.getConnect(mySqlConnect)

