#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/6/27
import re


def check_passwd(pwd):
    check_p = re.compile("^[a-zA-Z0-9_]{6,20}$")
    return check_p.match(pwd)


if __name__ == '__main__':
    print check_passwd("123中123333")
