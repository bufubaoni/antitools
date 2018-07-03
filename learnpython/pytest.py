#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/10/18


class A(object):
    a = 'a'

    def __init__(self, b):
        self.b = b


if __name__ == '__main__':
    a = A('test a')
    print (a.b)
    print (a.a)
    a.a = 'asdasdf'
    b = A('test b')
    print (b.b)
    print (b.a)
