#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/16
handle = open('test.txt')
nstr=handle.read()
print nstr
handle.tell()
for line in handle:
    print line

handle.close()
