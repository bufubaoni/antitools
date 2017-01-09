#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/9
import ConfigParser

conf = ConfigParser.ConfigParser()
conf.readfp(open("init.conf"))

DB_URL = conf.get("mysql", "url")

VERSON_FILE_NAME = conf.get("versonfile", "filename")

OUTPUT_EXCEL = conf.get("excelfile", "filename")
