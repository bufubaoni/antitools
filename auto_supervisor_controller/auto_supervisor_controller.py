#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/9/5
import requests
from requests.auth import HTTPBasicAuth
import os
import sys

print sys.path
session = requests.Session()
res = session.get('http://192.168.1.109:9001/?processname=jetty&amp;action=restart',
                  auth=HTTPBasicAuth('alex', '123456'))





