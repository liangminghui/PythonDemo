#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 多线程工具类
import time
import threading

count1 = 0  # 正确加锁方式初始值
count2 = 0  # 不加锁
count3 = 0  # 错误的加锁方式初始值

iter_times = 1000000  # 累加次数


# 加锁
def target_function(lock):
    global count1, iter_times
    lock.acquire()
    # do something... 养成好习惯，万一报错了要释放锁！
    try:
        for i in range(iter_times):
            count1 += 1
        # time.sleep(1)
        print(threading.current_thread())
    finally:
        lock.release()


# 不加锁
def target_function2():
    global count2, iter_times
    for i in range(iter_times):
        count2 += 1
    print(threading.current_thread())


# 加了个假锁
def target_function3():
    global count3, iter_times
    lock = threading.Lock()
    lock.acquire()
    # do something... 养成好习惯，万一报错了要释放锁！
    try:
        for i in range(iter_times):
            count3 += 1
        # time.sleep(1)
        print(threading.current_thread())
    finally:
        lock.release()


'''
   控制数数据库连接上数
   maxconnections = 5
   pool_sema = BoundedSemaphore(value=maxconnections)
   pool_sema.acquire()
   conn = connectdb()
   ... use connection ...
   conn.close()
   pool_sema.release()
 '''


def main():
    lock = threading.Lock()
    print(threading.current_thread())
    name = 't'
    for i in range(5):
        name_i = name + str(i)
        t1 = threading.Thread(target=target_function, name=name_i, args=[lock])
        t2 = threading.Thread(target=target_function2, name=name_i)
        t3 = threading.Thread(target=target_function3, name=name_i)
        t1.start()
        t2.start()
        t3.start()
    time.sleep(10)
    print(count1)
    print(count2)
    print(count3)


if __name__ == '__main__':
    main()
