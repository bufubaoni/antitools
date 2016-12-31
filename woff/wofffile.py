#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/12/31
import requests
from pyquery import PyQuery as pq
from blinker import signal
import json

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


num = set()


@numb_signal.connect
def c(s):
    for item in s.__repr__().split("\u"):
        item.strip(".")
        if len(item) == 4:
            num.add(item)
    return num


@save_file_signal.connect
def save_file(s):
    with open("num.txt", "a") as f:
        f.write(json.dumps(list(num)) + "\n")


if __name__ == "__main__":
    get_numb()
