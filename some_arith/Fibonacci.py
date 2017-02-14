#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fibonac(step):
    a = 0
    b = 1
    c = 1
    n = 0
    while step > n:
        if n == 0:
            yield 0
        elif n == 1:
            b = 1
            a = 1
            yield a
        else:
            c = a + b
            a = b
            b = cz

            yield a

        n += 1


for i in fibonac(14):
    print i
