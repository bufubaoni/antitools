#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/12/31
import requests
from pyquery import PyQuery as pq
from blinker import signal
import json
from collections import OrderedDict
import xml.etree.ElementTree as ET

from woff2otf import convert
from fontTools.ttLib import TTFont

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
        print (title, convert_number(number_total), convert_number(number_realtime))
    save_file_signal.send("go")


def get_woff_url():
    woffs = pq(content.text)("style")
    for line in woffs.text().split("\n"):
        if "woff" in line:
            return line.split(")")[0].strip()[5:-1]


def convert_number(s):
    url = get_woff_url()
    wof = save_woff(url)
    otf = convent2otf(wof)
    xml = convert2xml(otf)
    _dict = par_xml(xml)
    _lst_uicode = []
    for item in s.__repr__().split("\u"):
        _lst_uicode.append("uni" + item[:4].upper())
        if item[4:]:
            _lst_uicode.append(item[4:])
    _lst_uicode = _lst_uicode[1:-1]
    return "".join([_dict[i] for i in _lst_uicode])


def save_woff(url):
    path = "test.woff"
    with open(path, "wb") as f:
        for buck in sesson.get(url, stream=True):
            f.write(buck)
    return path


def convent2otf(path):
    outpath = "test.otf"
    convert(path, outpath)
    return outpath


def par_xml(path):
    root = ET.parse(path)
    _numbs = dict()
    numbs = root.iter("GlyphID")
    for numb in numbs:
        if len(numb.get("name")) == 7:
            _numbs[numb.get("name")] = str(int(numb.get("id")) - 2)
    _numbs["."] = "."
    return _numbs


def convert2xml(path):
    ttl = TTFont(path)
    path = "test.xml"
    ttl.saveXML(path)
    return path


if __name__ == "__main__":
    get_numb()
