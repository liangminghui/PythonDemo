#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 多线程案例脏读数据
import threading, logging
import os.path
import os

logging.basicConfig(level=logging.INFO)
READ_FILE_SIZE = 4
thread_loacl = threading.local()


# python多线程读取文件
# 单线程读取
# def readFile():
#     try:
#         with open("IODemo.txt","r",encoding="UTF-8",errors="ignored") as file:
#             for i in file:
#                 print(i)
#     finally:
#         print("读取结束")
#
#
# t1 = threading.Thread(target=readFile)
# t1.start()
# t1.join()
def create_thread(thread_count):
    print("将要开始创建%d个线程" % thread_count)
    thread_count_index = 0
    while thread_count_index < thread_count:
        thread_count_index = thread_count_index + 1
        print("开始创建第%d个线程" % thread_count_index)
        t = threading.Thread(target=thread_read_file, args=(thread_count_index,), name="thread_%d" % thread_count_index)
        t.start()
        t.join()


def thread_read_file(thread_count_index):
    print(threading.current_thread().getName() + "正在读取。。。")
    read_file_from = (thread_count_index - 1) * READ_FILE_SIZE
    readFile = open("IODemo.txt", "rb")
    readFile.seek(read_file_from, 1)
    print(readFile.read(READ_FILE_SIZE))
    print(threading.current_thread().getName() + "读取结束。。。")
    readFile.close()


def more_thread_io():
    fileSize = os.path.getsize("IODemo.txt")
    thread_count = int(fileSize / READ_FILE_SIZE)
    if (fileSize % READ_FILE_SIZE > 0):
        thread_count = thread_count + 1
    create_thread(thread_count)


more_thread_io()
# balance = 0
# lock = threading.Lock()
# balanceLock = 0
# def change(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     for i in range(100000):
#         #未加锁
#         #lockChange(n)
#         #加锁之后的现象
#         lock.acquire()
#         try :
#             lockChange(n)
#         except Exception as e:
#             logging.INFO(e)
#         finally:
#             lock.release()
#
#
# def lockChange(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
#
#
# t1 = threading.Thread(target=run_thread, args=(1,))
# t2 = threading.Thread(target=run_thread, args=(3,))
# t3 = threading.Thread(target=run_thread, args=(5,))
# t4 = threading.Thread(target=run_thread, args=(7,))
# t5 = threading.Thread(target=run_thread, args=(9,))
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()
# print(balance)
# thread_loacl = threading.local()
#
#
# def process_name():
#     person = thread_loacl.person
#     print("%s is in %s" % (person, threading.current_thread().getName()))
#
#
# def process_thread(name):
#     thread_loacl.person = name
#     process_name()
#
#
# t1 = threading.Thread(target=process_thread, args=("lmh",), name="thread 1")
# t2 = threading.Thread(target=process_thread, args=("lmh2",), name="thread 2")
# t3 = threading.Thread(target=process_thread, args=("lmh3",), name="thread 3")
#
# t1.start()
# t1.join()
# t2.start()
# t2.join()
# t3.start()
# t3.join()
