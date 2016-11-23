#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/11/11
from datetime import datetime, timedelta
import time

s = '''
a 1
b 2
a 4
b 6
'''
d = dict()
for item in s.strip().split("\n"):
    (key, value) = item.split(" ")


def testtime(fn):


    def wrapp(*args, **kwargs):
        print("start time ----- {time}".format(time=time.time()))
        temp = fn(*args, **kwargs)
        print("stop time ----- {time}".format(time=time.time()))
        return temp

    return wrapp


@testtime
def dateaddmonth(datetime, month):
    day = datetime.day
    for i in range(0, month):
        datetime = (datetime + timedelta(days=31)).replace(day=day)
    return datetime


@testtime
def otherdateaddmonth(datetime, month):
    return datetime + timedelta(month * 365 / 12)


if __name__ == "__main__":
    print(dateaddmonth(datetime.now(), 90000))
    time.sleep(1)
    print(otherdateaddmonth(datetime.now(), 90000))
