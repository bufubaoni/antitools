#!/usr/bin/env python
# -*- coding: utf-8 -*-


# def fibonac(step):
#     a = 0
#     b = 1
#     n = 0
#     while step > n:
#         a, b = b, a + b
#         yield b
#
#         n += 1

if __name__ == "__main__":
    # for i in fibonac(11):
    #     print i
    T = map(lambda x: " ".join(map(lambda y: "{}*{}={}".format(y, x, y * x), range(1, x+1))), range(1, 10))
    print "\n".join(T)
    # print reduce(lambda x: x*x, range(1, 10))