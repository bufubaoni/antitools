#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/9/6

B = [2, 3, 4, 5, 6, 7, 8, 2, 3]
A = [1, [2, 3, [2, 3]], [4, 5, 6], 7]


_count = iter(range(0, len(B)))
def B2A(template, input):
    return [B2A(lst, input) if isinstance(lst, list) else input[next(_count)] for lst in template]

if __name__ == '__main__':
    print("A------> {a}".format(a=A))
    print("B------> {a}".format(a=B))
    print("B2A----> {a}".format(a=B2A(A, B)))
