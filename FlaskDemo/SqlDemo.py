#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import sqlite3;
conn=sqlite3.connect("../DBDemo/test.db")
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import Column,String,INT,create_engine,ForeignKey
import Password

#定义class对象
Base=declarative_base()
class User(Base):
    __tablename__='user'
    id=Column(String(20),primary_key=True)
    name=Column(String(200))
    score=Column(INT)
    password=Column(String(200))
    book=relationship('Book')

class Book(Base):
    __tablename__='book'
    id=Column(String(20),primary_key=True)
    name=Column(String(200))
    user_id=Column(String(20),ForeignKey('user.id'))



#初始化链接
engine=create_engine('sqlite:///../DBDemo/test.db')
DBSession=sessionmaker(bind=engine)
session=DBSession()
#用户Adam 密码123
#验证登录
def login(userName,password):
    try:
        #暂时不验证
        userAll=session.query(User).filter(User.name==userName).all()
        i =  len(userAll);
        if i==0:
            return False,"没有姓名为%s的用户"%userName
        elif i==1:
            #加密填入的密码，与数据库的密码比较
            user=userAll[0]
            if Password.encrypted(password)==user.password:
                return True,user
            else:
                return False,"账号验证未通过"
        else :
            return False,"存在多个姓名为%s的用户"%userName


    except BaseException as e:
        print(e)
    finally:
        session.close()

#获取用户信息
def getUsersBookInfo(userId):
    book=session.query(Book).filter(User.id==userId).all()
    return book