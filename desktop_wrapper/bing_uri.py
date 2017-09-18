#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/9/18
from requests import Session
import re

base_path = "C:/Users/Public/Pictures/Sample Pictures/"

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


def save_img(url):
    file_name = url.split("/")[-1]
    path = base_path + file_name
    with open(path, "wb") as fd:
        for chunk in session.get(url, stream=True):
            fd.write(chunk)

    bmp_path = base_path + file_name.split(".")[0] + ".bmp"
    path = jpg2bmp(path, bmp_path)
    return path


def jpg2bmp(in_path, out_path):
    from PIL import Image
    import os
    bmp = Image.open(in_path)
    r, g, b = bmp.split()
    img = Image.merge("RGB", (r, g, b))
    img.save(out_path)
    os.remove(in_path)
    return out_path


def save_wrapper(uri):
    uri = get_uri(uri)

    path = save_img(uri)

    return path


if __name__ == '__main__':
    print get_uri(uri)
