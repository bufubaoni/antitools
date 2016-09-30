#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/9/30
from bottle import route, post, request
import bottle
import pdb

app = bottle.default_app()


@route("/upload")
def upload():
    if request.method.lower() == "port":
        pdb.set_trace()
    else:
        return "upload"


if __name__ == '__main__':
    bottle.run(app=app, host="0.0.0.0", port=8000)
