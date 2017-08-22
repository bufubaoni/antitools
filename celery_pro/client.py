#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/8/18
from celery_test import add

# print add.delay(12,15)

from base64 import b64decode
import pickle

print pickle.loads(b64decode("gAJ9cQEoVQZzdGF0dXNxAlUHU1VDQ0VTU3EDVQl0cmFjZWJhY2txBE5VBnJlc3VsdHEFSxlVB3Rhc2tfaWRxBlUkNmQ5YmVkMGEtNGNmZi00ZTJiLWE3MDgtNzMyNTUwYWI4MzYzcQdVCGNoaWxkcmVucQhddS4="))