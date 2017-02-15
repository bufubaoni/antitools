#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fibonac(step):
    a = 0
    b = 1
    n = 0
    while step > n:
        yield a
        a, b = b, a+b
        n += 1
