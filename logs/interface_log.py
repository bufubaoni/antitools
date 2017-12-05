#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/12/5
import re

with open("fubang_9005.log", "r") as f:
    for i, line_get in enumerate(f.readlines()):
        line_get = re.findall("127\.0\.0\.1 - - .+[GET,POST] .+", line_get)
        if line_get:
            time_len = line_get[0].split()[-1]
            if float(time_len) > 1:
                print line_get[0].split()[3],line_get[0].split()[4],line_get[0].split()[5].strip('"'), line_get[0].split()[6],time_len
