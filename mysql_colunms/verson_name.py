#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/11/30
import json


def get_P(name=""):
    return load_Conf().get(name)


def push_P(name=""):
    if not get_P(name):
        tem = load_Conf()
        tem[name] = name
        dumps_Conf(conf=tem)


def load_Conf(filename="verson.json"):
    f = open(filename, "r")
    tem = "".join(f.readlines())
    T = json.loads(tem)
    f.close()
    return T


def dumps_Conf(filename="verson.json", conf={}):
    f = open(filename, "w")
    f.write(json.dumps(conf))
    f.close()


if __name__ == "__main__":
    # dumps_Conf()
    print(load_Conf())
    print(get_P("test1"))
    push_P("test1")
