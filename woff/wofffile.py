#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/12/31
import requests
from pyquery import PyQuery as pq
from blinker import signal
import json
from collections import OrderedDict


from woff2otf import convert_streams
numb_signal = signal("numb")
save_file_signal = signal("save")
sesson = requests.Session()
url = "http://maoyan.com/board/1"
content = sesson.get(url)

dds = pq(content.text)("dl.board-wrapper>dd")


def get_numb():
    for dd in dds:
        tdd = pq(dd)
        title = tdd("div>div>div.movie-item-info>p.name").text()
        number_realtime = tdd("div>div>div.movie-item-number>p.realtime>span>span.stonefont").text()
        number_total = tdd("div>div>div.movie-item-number>p.total-boxoffice>span>span.stonefont").text()
        numb_signal.send(number_total)
        numb_signal.send(number_realtime)
        print (title, number_total, number_realtime)
    save_file_signal.send("go")

def get_woff_url():
    woffs=pq(content.text)("style")
    for line in woffs.text().split("\n"):
        if "woff" in line:
            return line.split(")")[0].strip()[5:-1]


num = set()


@numb_signal.connect
def c(s):
    for item in s.__repr__().split("\u"):
        item.strip(".")
        if len(item) == 4:
            num.add(item)
    return num

def save_woff(url):
    path = "test.woff"
    with open(path,"wb") as f:
        for buck in sesson.get(url):
            f.write(buck)
    return path

def convent2otf(path):
    outpath = "test.otf"
    convert_streams(path,outpath)

@save_file_signal.connect
def save_file(s):
    with open("num.txt", "a") as f:
        p = list(num)
        p.sort()
        od = OrderedDict(sorted({item: item for item in p}.items(), key=lambda t: t[0]))
        f.write(json.dumps(od) + "\n")


if __name__ == "__main__":
    save_file(get_woff_url())
