import time, threading


def loop():
    print("thread %s is running" % threading.current_thread().getName())
    n = 0
    while n<5:
        n = n + 1
        print("theread %s>>>%s" % (threading.current_thread().getName(), n))
        time.sleep(1)
    print("thread %s is end" % threading.current_thread().getName())


print("thread %s is running" % threading.current_thread().getName())
t = threading.Thread(target=loop, name="LoopThread")
t.start()
t.join()
print("thread %s is end" % threading.current_thread().getName())

# def loop():
#     print("Thread %s is running" % threading.current_thread().getName())
#     n = 0;
#     while n < 5:
#         n = n + 1
#         print("Thread %s>>>%s" % (threading.current_thread().getName(), n))
#         time.sleep(1)
#     print("Thread %s is end " % threading.current_thread().getName())
#
#
# print("Thread %s is running" % threading.current_thread().getName())
# t = threading.Thread(target=loop, name="LoopThread")
# t.start()
# t.join()
# print("Thread %s is end" % threading.current_thread().getName())
