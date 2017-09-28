#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/9/27
from flask import Flask
from requests import Session
from datetime import datetime


apply_time = datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]

session = Session()

opendoor_url = "http://acs.corelines.cn/phone/v1/home/door/initiative/access?" \
               "room_node_id=20232&household_id=9308&apply_time={apply_time}" \
               "&transaction_no=a201709271615285909308&" \
               "code=9278A73B33124F182260994879203CB332A1BDE3AB69CD1CD8073C52A5D010F3" \
               "&door_id=10364&household_token=e056df6d1c90478892b3c934ebae711d".format(apply_time=apply_time)

load_url = "http://acs.corelines.cn/phone/v1/my/version/load"
load_body = "app_platform=1&apply_time=20170927172443521&" \
            "app_name=acs_phone_android&" \
            "code=B041597F4FC3CF828314B73269B546EC0A2690B03AF21E101B19D6E0CAF88548".format(apply_time=apply_time)
session.headers = {}

acckey_url = "http://acs.corelines.cn/phone/v1/home/visiting/password/add?" \
             "room_node_id=20232&household_token=e056df6d1c90478892b3c934ebae711d&visiting_time={visiting_time}" \
             "&household_id=9308&apply_time=20170927173736609&visiting_name=&" \
             "code=19DE0F7F0F65F10099B0FCB506E652FCE466F89048CD6F502CE287DE55A9D86C&visiting_phone=".format(visiting_time=apply_time)

app = Flask(__name__)


def opare_door(url):
    print url
    return session.post(url).text


@app.route('/get_key')
def hello_world():
    return opare_door(acckey_url)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
