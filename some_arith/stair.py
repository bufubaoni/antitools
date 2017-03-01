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


def stair2(n):
    a = 1
    b = 2
    c = 4
    step = 0
    while n > step:
        yield a
        a, b, c = b, c, a+b+c
        step += 1


if __name__ == "__main__":
    print stair(6)
    for i in stair2(6):
        print i
