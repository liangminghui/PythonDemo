#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#ORM技术：Object-Relational Mapping
from sqlalchemy import Column,String,create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
import sqlite3
conn=sqlite3.connect("test.db")
cursor=conn.cursor()
select=cursor.execute("select * from user")

#create=cursor.execute("create table book(id varchar (20) primary key ,name varchar (200),user_id varchar (20))")
#insrt=cursor.execute("insert into book(id,name,user_id) values ('B-002','安徒生童话','A-001')")
select=cursor.execute('select * from book')
#print(select.fetchall())
cursor.close()
conn.commit()
conn.close()
#创建对象基本类
Base=declarative_base()
#定义User对象
class User(Base):
    #表名
    __tablename__='user'
    #字段
    id=Column(String(20),primary_key=True)
    name=Column(String(200))
    book=relationship('Book')
class Book(Base):
    #表名
    __tablename__='book'
    #字段
    id=Column(String(20),primary_key=True)
    name=Column(String(200))
    #设置外联键
    user_id=Column(String(20),ForeignKey('user.id'))

#初始化数据库连接
#engine=create_engine('mysql+pymysql://root:supporter@localhost:3306/springboot')
engine=create_engine('sqlite:///test.db')
DBSession=sessionmaker(bind=engine)
#使用session操作数据
session=DBSession()
user=session.query(User).filter(User.id=='A-001').one()
#print('type',type(user))
#print('name',user.name)
for book in user.book:
    print(book.id)
session.close()
#一对多demo
