#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/7/20
import redis

r = redis.StrictRedis(host="192.168.85.130", port=6379, db=0)

# r.set("name", "12333333",10)
# r.expire("name", 10)
print r.get("name")
