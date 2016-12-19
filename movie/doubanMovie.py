#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/10/26
import requests
import time
import random
from pyquery import PyQuery as pq
session = requests.Session()
url = "https://movie.douban.com/top250"
session.get(url)
for i in range(0,10):
    if i == 0:
        print i
    else:
        print i * 25
    print random.random(10)

if __name__ == '__main__':
    pass