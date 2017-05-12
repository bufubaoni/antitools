#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/5/4
# from foolq import test, TEST
# import foolq
# foolq.TEST = "dynimac"
#
# test()
# from multiprocessing import Process,Pool
import time
#
def loop():
    while True:
        print "this is event loop"
        time.sleep(5)

#
# proc = Process(target=loop,args=())
# proc.start()
#
# print "haha"
# from multiprocessing import Pool
#
# def f(x):
#     return x*x
#
# if __name__ == '__main__':
#     p = Pool(5)
#     print(p.map(f, [1, 2, 3]))
# from multiprocessing import Process
#
#
# def f(name):
#     while True:
#         print 'hello', name
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()
#     print "ok"

from threading import Thread
t = Thread(target=loop)
t.start()
print "haha "
