#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/12/28
import logging
import logging.config
import json
import os

import requests

logging.config.fileConfig("logging.conf")
logger = logging.getLogger("save")

baseurl = "http://img.hb.aicdn.com/"
extenturl = "fw658"
basedir = "download/"


def _get_file_url(baseurl, pin, extenturl):
    url = baseurl + "/" + pin.get("file").get("key") + "_" + extenturl
    return url


def _get_file_extend(pin):
    ext = "." + pin.get("file").get("type").split("/")[1]
    logger.debug(ext)
    return ext


def save_file(pin, baseurl=baseurl, extenturl=extenturl, basedir=basedir):
    url = _get_file_url(baseurl, pin, extenturl)
    ext = _get_file_extend(pin)
    file_name = str(pin.get("file").get("id")) + ext
    path = basedir + file_name
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    if not os.path.exists(path):
        with open(path, "wb") as fd:
            for chunk in requests.get(url, stream=True):
                fd.write(chunk)
    else:
        logger.debug("exists")


if __name__ == "__main__":
    pin = ('''{
      "pin_id": 908666605,
      "user_id": 13250280,
      "board_id": 15759013,
      "file_id": 114482204,
      "file": {
        "id": 114482204,
        "farm": "farm1",
        "bucket": "hbimg",
        "key": "a6a6869b8e190ffd2be75501fa21e6c66930410113354-tvl7D0",
        "type": "image/jpeg",
        "height": "915",
        "width": "610",
        "frames": "1",
        "colors": [
          {
            "color": 3355443,
            "ratio": 0.13
          }
        ],
        "theme": "333333"
      },
      "media_type": 0,
      "source": null,
      "link": null,
      "raw_text": "。",
      "text_meta": {},
      "via": 863794384,
      "via_user_id": 8810001,
      "original": 860693607,
      "created_at": 1478187239,
      "like_count": 0,
      "comment_count": 0,
      "repin_count": 0,
      "is_private": 0,
      "orig_source": null,
      "hide_origin": true
    }''')
    pin = json.loads(pin)
    save_file(pin)
