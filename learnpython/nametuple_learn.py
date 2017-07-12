#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/7/12
from collections import namedtuple

Test = namedtuple("test", ["a", "b"])

test = Test(a=1, b=2)

_test = test._replace(a=3)

print id(test)
print id(_test)

test = {"a": 1,
        "b": 2}

_test = test.update(a=3)

print id(test)
print id(_test)
