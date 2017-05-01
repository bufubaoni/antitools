#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fibonac(step):
    a = 0
    b = 1
    n = 0
    while step > n:
        a, b = b, a + b
        yield b
        n += 1

if __name__ == "__main__":
    pass