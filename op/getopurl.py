#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def geturl(str):
    with open("op.txt", "r") as f:
        lsurl = []
        for line in f.readlines():
            numb, url = line.split(" ")
            lsurl.append((numb,
                          url.strip(),
                          "op" + numb + "." + url.split(".")[-1].strip()))

if __name__ == "__main__":
    geturl(666)
