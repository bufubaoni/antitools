#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/3
# test1 to test2
# test1 -> (test1,test2)
# test2 -> (test1,test3,test4)
from pydal import DAL, Field

db_s = DAL("mysql://root:1308200@localhost/test1", db_codec='utf-8')

db_s.define_table("test1",
                  Field("test1"),
                  Field("test2"),
                  primarykey=[],
                  migrate=False)
