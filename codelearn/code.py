#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/15
import json

strmap = {"test": "中文"}
with open("test.json", "w") as f:
    f.write(json.dumps(strmap, ensure_ascii=False))
