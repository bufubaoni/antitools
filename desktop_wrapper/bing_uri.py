#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/9/18
from requests import Session
import re
import pdb

img = "g_img=\{.+\"(.+\.jpg)\""

uri = "http://www.bing.com"

session = Session()


def get_text(uri=uri):
    return session.get(uri).text


def get_img(string):
    rs = re.findall(img, string=string)
    if rs:
        return rs[0]

def get_uri(uri):
    return uri + get_img(get_text(uri))


if __name__ == '__main__':
    print get_uri(uri)
