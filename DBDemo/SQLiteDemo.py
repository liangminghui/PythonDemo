#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#sqlite(嵌入式数据库，数据库以文件形式存在)Demo
import sqlite3
#如果没有这个文件会新建
conn=sqlite3.connect("sqllite.db");
#创建cursor
cursor=conn.cursor();
#cursor.excute(sql)
#create=cursor.execute("create table user(id varchar(20) primary key ,nickname varchar(200))")
# insert=cursor.execute("insert into user (id,nickname) values"
#                       "('3','lmh')")
select=cursor.execute("select * from user")
print(select.fetchall())
cursor.close()
conn.commit()
conn.close()