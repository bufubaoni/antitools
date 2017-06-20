#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Queue

queue = Queue(maxsize=10)

queue.put("queue_test")
queue.put("test1")

if __name__ == "__main__":
    print queue.get()
    print queue.get()
    print queue.get()