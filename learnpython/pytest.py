#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/10/18
def attr():
    setattr(attr, "dict0", 1)
    print getattr(attr, "dict0")
    print locals()


if __name__ == '__main__':
    pd = attr()
    print type(pd)
