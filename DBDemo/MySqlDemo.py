#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#mysqlDemo，
#升级下载工具
# python -m pip install --upgrade pip
#pip install pymysql
import pymysql;
conn=pymysql.connect(host='127.0.0.1',port=3306,user="root",password="supporter",database="springboot");
cursor=conn.cursor();
select = cursor.execute("select * from sys_user where userId = '%d'"%1)
print(cursor.fetchall())
cursor.close()
conn.commit()
conn.close()

