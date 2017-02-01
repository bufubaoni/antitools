#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/29
from bottle import route,run,Bottle
from run import run

app = Bottle()


@app.route("/hello")
def index():
    return dict(name="hello alex")

run(app, host="127.0.0.1", port=8000)
