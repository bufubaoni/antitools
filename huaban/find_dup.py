#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/12/29
import json
"""just a file but no use in this flow"""
count = dict()

url = "http://img.hb.aicdn.com/{key}_fw658.{ext}"

alla = []


def find_dup(count):
    '''
    find the json file duplicate content

    Returns app board all an no duplication content

    Args:
        count: content of file by spider crawing
    '''
    with open("pins1.txt", "r") as f:
        while True:
            try:
                s = json.loads(f.next())
            except:
                break
            else:
                count[s.get("pin_id")] = 1
                alla.append(s.get("pin_id"))
    return count, alla


if __name__ == '__main__':
    (count, alla) = find_dup(count)
    print(len(count))
    print(len(alla))
    for item in alla:
        count[item] += 1

    for k, v in count.items():
        if v > 2:
            print("{k}: {v}".format(k=k, v=v))
