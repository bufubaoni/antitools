#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/11/30
from pydal import DAL, Field
from ConfPars import DB_URL
sys_tab = DAL(DB_URL)

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
    print sys_tab(sys_tab.COLUMNS.TABLE_SCHEMA == "test").select()

