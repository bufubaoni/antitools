#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/11/30
import json
import os
from ConfPars import VERSON_FILE_NAME

def get_P(name=""):
    return load_Conf().get(name)


def push_P(name=""):
    if not get_P(name):
        tem = load_Conf()
        tem[name] = name
        dumps_Conf(conf=tem)


def load_Conf(filename=VERSON_FILE_NAME):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            tem = "".join(f.readlines())
            if tem:
                T = json.loads(tem)
            else:
                T = dict()
    else:
        T = dict()
    return T


def dumps_Conf(filename=VERSON_FILE_NAME, conf={}):
    with open(filename, "w") as f:
        f.write(json.dumps(conf))



if __name__ == "__main__":
    # dumps_Conf()
    print(load_Conf())
    print(get_P("logintime"))
    push_P("logintime")
