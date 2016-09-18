#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/9/18
import logging


def task_log(task):

    # FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
    # logging.basicConfig(format=FORMAT)
    # log = logging.getLogger("ok")
    # log.setLevel(logging.DEBUG)
    # log.info(task)
    # log.info("asldkfj")
    print(task)
    def decorator(*a, **k):
        print(a)
        print(k)
        return task(*a, **k)
    return decorator

@task_log
def test(a):
    print(a)
    return a

if __name__ == '__main__':
    print(test("asdffff"))
