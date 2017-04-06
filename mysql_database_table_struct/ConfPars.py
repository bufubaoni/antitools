#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/9
import ConfigParser
import json


conf = ConfigParser.ConfigParser()
conf.readfp(open("init.conf"))

DB_URL = conf.get("mysql", "url")

VERSON_FILE_NAME = conf.get("versonfile", "filename")

OUTPUT_EXCEL = conf.get("excelfile", "filename")

DATABASENAME = conf.get("db2excel","databasename")

NO_NEED_TABLES = json.loads(conf.get("db2excel","noneedtables"))