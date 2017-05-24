#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/5/24
a=[]
b=[]
dic = {1:a,
       2:b,
       3:a}

dic[1].append(1)
dic[2].append(2)
dic[2].append(1)
dic[3].append(2)
dic[3].append(1)
dic[3].append(3)

print dic