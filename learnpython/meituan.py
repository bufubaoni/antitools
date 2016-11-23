#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/11/11
from datetime import datetime, timedelta

s = '''
a 1
b 2
a 4
b 6
'''
d = dict()
for item in s.strip().split("\n"):
    (key, value) = item.split(" ")


def dateaddmonth(datetime, month):
    day = datetime.day
    for i in range(0, month):
        datetime = (datetime + timedelta(days=31)).replace(day=day)
    return datetime


if __name__ == "__main__":
    print(dateaddmonth(datetime.now(), 9))
