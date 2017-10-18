#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/10/18
from gevent import monkey

monkey.patch_all()

import gevent

from requests import Session
import json
from datetime import datetime, timedelta

data = {"receiveTime": datetime.now(), "hostNumber": "2233"}
session = Session()
url = "http://xxxx/web/v3/pub/fault_alarm/"
hosts = []

with open("dtu_id.json", "r") as f:
    dtus = "".join(f.readlines())
    hosts = json.loads(dtus)

import random

print hosts
a =[]
for i in range(0, 1000):
    dtu_index = random.randint(0, len(hosts) - 1)
    data["receiveTime"] = (data["receiveTime"] + timedelta(days=i)).strftime("%Y-%m-%d %H:%M:%S")
    data["hostNumber"] = hosts[dtu_index]
    print data
    content = gevent.spawn(session.post, url, json.dumps(data))
    a.append(content)
    data["receiveTime"] = datetime.now()


gevent.joinall(a)