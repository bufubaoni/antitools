#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/9/27
import os
from requests import Session

session = Session()
car_name = "FiddlerRoot.cer"

file_path = os.path.dirname(__file__)

cer_file = os.path.join(file_path, car_name)
print os.path.exists(cer_file)
session.verify = cer_file
