#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/6
class A(object):
    def saysome(self):
        print "this is A"


if __name__ == '__main__':
    a = getattr(A, "saysome")
    a
