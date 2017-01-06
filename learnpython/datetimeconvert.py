#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/4
from datetime import datetime

dt = datetime.strptime("20161215", "%Y%m%d")
print dt

module = __import__("getinstance")
class_ = getattr(module, "A")
instance = class_()
instance.saysome()