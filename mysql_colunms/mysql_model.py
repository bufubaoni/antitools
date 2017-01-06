#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/11/30
from pydal import DAL, Field

sys_tab = DAL("mysql://user:passwd@127.0.0.1/information_schema")

sys_tab.define_table('COLUMNS',
                     Field("TABLE_SCHEMA", ),
                     Field("TABLE_NAME"),
                     Field("COLUMN_NAME"),
                     Field("IS_NULLABLE"),
                     Field("DATA_TYPE"),
                     Field("COLUMN_TYPE"),
                     primarykey=[],
                     migrate=False)
if __name__ == "__main__":
    print sys_tab(sys_tab.COLUMNS.TABLE_SCHEMA == "test1").select()
    print sys_tab._lastsql
