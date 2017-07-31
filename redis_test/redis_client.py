#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/7/20
import redis

r = redis.StrictRedis(host="192.168.85.130", port=6379, db=0)

# r.set("key", [])
# r.expire("name", 10)
# r.append("key","dddddd")
r.sadd("a","asdf")
# print r["a"]
# print r.smembers("info_fire_authorities")
print r.sismember("a","b")
r.delete("info_manometer")
print r.smembers("info_manometer")