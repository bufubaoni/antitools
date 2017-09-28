#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/9/27
from flask import Flask
from requests import Session
from datetime import datetime


apply_time = datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]

session = Session()



app = Flask(__name__)


def opare_door(url):
    print url
    return session.post(url).text


@app.route('/get_key')
def hello_world():
    return opare_door(session)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
