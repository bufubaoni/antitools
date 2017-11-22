#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/11/22
from task_and_coroutines import share_task




@share_task
def test_task():
    import time
    time.sleep(5)
    print "task from other pro"

#
if __name__ == '__main__':
    test_task()
#     _class = __import__("task_test")
#     method = getattr(_class, "test_task")
#     method()
