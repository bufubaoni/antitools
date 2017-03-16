#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/10/26
# lower 40 requests per min
import time
import random

import requests
from prettytable import PrettyTable
from pyquery import PyQuery as pq

pt = PrettyTable()
pt.field_names=[u"编号",u"名称"]
pt.align[u"名称"]="l"
session = requests.Session()

for i in range(0,10):
    url = "https://movie.douban.com/top250"
    if i == 0:
        data = ""
    else:
        data = "?start={start}&filter=".format(start=i * 25)
    url += data
    content = session.get(url).content
    map(pt.add_row,[(pq(row)("div.pic>em").text(),
                     pq(row)("div.info>div.hd>a").text().encode("utf8"))
                        for row in pq(content)("ol.grid_view>li>div.item")])
    sleep = random.randrange(20)
    print("page {page},----sleep({sleep})".format(page=i,sleep=sleep))
    time.sleep(sleep)
with open("movie.txt","a") as f:
    f.write(str(pt))
