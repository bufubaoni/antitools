#!/usr/bin/env python
# -*- coding: utf-8 -*-


def stair(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return stair(n - 1) + stair(n - 2) + stair(n - 3)


def stair2():
    a = 1
    b = 2
    c = 4
    while True:
        yield a
        a, b, c = b, c, a+b+c


if __name__ == "__main__":
    print stair(6)
    s = stair2()
    for i in range(0,6):
        print s.next()
