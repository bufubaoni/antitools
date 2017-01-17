#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/11/30
import json
import os
from ConfPars import VERSON_FILE_NAME


def get_P(name=""):
    """

    :param name: get clunm's name or table's name
    :return: labal local langage
    """
    return load_Conf().get(name)


def push_P(name=""):
    """
    :param name: clunm's name or table's name
    """
    if not get_P(name):
        tem = load_Conf()
        tem[name] = name
        dumps_Conf(conf=tem)


def load_Conf(filename=VERSON_FILE_NAME):
    """

    :param config the verbson filename:
    :return: dict clunm's name and vobern's name
    """
    if os.path.exists(filename):
        with open(filename, "r") as f:
            tem = "".join(f.readlines())
            if tem:
                T = json.loads(tem)
            else:
                T = dict()
    else:
        with open(filename, "w") as f:
            T = dict()
            f.write(json.dumps(T))

    return T


def dumps_Conf(filename=VERSON_FILE_NAME, conf={}):
    """

    :param filename: conf dumps json file
    :param conf: dict clunm's name and vobern's name
    """
    with open(filename, "w") as f:
        f.write(json.dumps(conf))


if __name__ == "__main__":
    print(load_Conf())
    print(get_P("logintime"))
    push_P("logintime")
