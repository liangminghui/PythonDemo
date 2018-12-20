#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import sqlite3
conn=sqlite3.connect("../DBDemo/test.db")
cursor=conn.cursor()
# modify=cursor.execute("alter table user add password varchar(200)")
# update =cursor.execute("update user set password='5LKH9UXHiCx45rAXcjM/dw=='")
select =cursor.execute("select * from user")
# print(select.fetchall())

def findUserByName(name):
    #处理sql
    sql="select * from user where name = '%s'"%name
    print(sql)
    select =cursor.execute(sql)
    print(select.fetchall())
findUserByName("Adam")
cursor.close()
conn.commit()
conn.close()

