#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/9
import ConfigParser
import json

conf = ConfigParser.ConfigParser()
conf.readfp(open("init.conf"))

DB_URL = conf.get("mysql", "url")

OUTPUT_FILE = conf.get("excelfile", "filename")

TABLES = json.loads(conf.get("tables", "tables"))

SCHEMA = conf.get("schema", "schema")
