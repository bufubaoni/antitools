#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/12/28
# http://huaban.com/boards/15759013/?qq-pf-to=pcqq.group&ix8ifcer&max=745069813&limit=20&wfl=1
# http://huaban.com/boards/15759013/?qq-pf-to=pcqq.group&ix8ifces&max=184558005&limit=20&wfl=1
import logging
import logging.config

import requests

from content_pars import pars

logging.config.fileConfig("logging.conf")
logger = logging.getLogger("huaban")

session = requests.Session()


def get_html_content(url):
    content = session.get(url)
    if content.ok:
        return content.text

def get_pins(pars):
    return pars.get("pins")




# print content.text

if __name__ == '__main__':
    url = "http://huaban.com/boards/15759013/"

    logger.debug(pars(get_html_content(url)))

