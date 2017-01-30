#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/29
from bottle import route ,run
from run import run


@route("/hello")
def index():
    return dict(name="hello alex")

run(host="127.0.0.1", port=8000)
