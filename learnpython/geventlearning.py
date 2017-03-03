#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gevent
import time


def foo():
    print("foo pre_exe")
    gevent.sleep(0)
    time.sleep(10)
    print("foo exe")


def good():
    print("good pre_exe")
    time.sleep(10)
    print("good exe")

gevent.joinall([gevent.spawn(foo), gevent.spawn(good)])