#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def geturl(str):
    with open("op.txt", "r") as f:
        print [(line.split(" ")[0], line.split(" ")[1].strip(),
                "op" + line.split(" ")[0] + '.' +
                line.split(" ")[1].strip().split('.')[-1],)
               for line in f.readlines()]


if __name__ == "__main__":
    geturl(666)
