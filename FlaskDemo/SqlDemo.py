#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import sqlite3;
conn=sqlite3.connect("../DBDemo/test.db")
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import Column,String,INT,create_engine,ForeignKey
#定义class对象
Base=declarative_base()
class User(Base):
    __tablename__="user"
    id=Column(String(20),primary_key=True)
    name=Column(String(200))
    score=Column(INT)
    book=relationship('Book')

class Book(Base):
    __tablename__="book"
    id=Column(String(20),primary_key=True)
    name=Column(String(200))
    user_id=Column(String(20),ForeignKey('user.id'))
#初始化链接
engine=create_engine('sqlite:///../DBDemo/test.db')
DBSession=sessionmaker(bind=engine)
session=DBSession()

#验证登录
def login(userName,password):
    book=session.query(Book).filter(Book.user_id=='A-001').all()
    return book
    pass
#获取用户信息
def getUsersBookInfo(userName):
    pass

print(login("",""));
