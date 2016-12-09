#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/12/9
from Queue import Queue
from threading import Thread
import time

q = Queue()


def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()


def do_work(key):
    time.sleep(2)
    print ("do work {key}\n".format(key=key))


for i in range(2):
    t = Thread(target=worker)
    t.daemon = True
    t.start()

for i in range(4):
    q.put(i)

q.join()
