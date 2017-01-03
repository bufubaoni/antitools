#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/12/31
import requests
from pyquery import PyQuery as pq
from blinker import signal

from readwoff import get_dict_numb_from_woff

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
        number_realtime = tdd(
            "div>div>div.movie-item-number>p.realtime>span>span.stonefont").text()
        number_total = tdd(
            "div>div>div.movie-item-number>p.total-boxoffice>span>span.stonefont").text()
        numb_signal.send(number_total)
        numb_signal.send(number_realtime)
        print (title, convert_number(number_total), convert_number(number_realtime))
    save_file_signal.send("go")


def get_woff_url():
    woffs = pq(content.text)("style")
    for line in woffs.text().split("\n"):
        if "woff" in line:
            return line.split(")")[0].strip()[5:-1]


def convert_number(s):
    url = get_woff_url()
    path = save_woff(url)
    _dict = get_dict_numb_from_woff(path)
    _lst_uincode = []
    for item in s.__repr__().split("\u"):
        _lst_uincode.append("uni" + item[:4].upper())
        if item[4:]:
            _lst_uincode.append(item[4:])
    _lst_uincode = _lst_uincode[1:-1]
    return "".join([_dict[i] for i in _lst_uincode])


def save_woff(url):
    path = "test.woff"
    with open(path, "wb") as f:
        for buck in sesson.get(url, stream=True):
            f.write(buck)
    return path


if __name__ == "__main__":
    get_numb()
