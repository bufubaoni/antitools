#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/6/28
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port=5000)
