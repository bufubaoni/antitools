#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/11/30
from mysql_model import sys_tab


def gettables(schema=None):
    if schema:
        tables = sys_tab(sys_tab.COLUMNS.TABLE_SCHEMA == schema). \
            select(sys_tab.COLUMNS.TABLE_NAME)
        return list(set([table.TABLE_NAME for table in tables]))
    else:
        return None


def getcolumns(table=None,schema=None):
    if table:
        columns = sys_tab((sys_tab.COLUMNS.TABLE_NAME == table) & (sys_tab.COLUMNS.TABLE_SCHEMA == schema)). \
            select(sys_tab.COLUMNS.COLUMN_NAME,
                   sys_tab.COLUMNS.IS_NULLABLE,
                   sys_tab.COLUMNS.DATA_TYPE,
                   sys_tab.COLUMNS.COLUMN_TYPE,
                   sys_tab.COLUMNS.TABLE_SCHEMA)
        return [(column.COLUMN_NAME,
                 column.IS_NULLABLE,
                 column.DATA_TYPE,
                 column.COLUMN_TYPE) for column in columns]


def getTableAndColumns(schema=None):
    return {tabel: getcolumns(table=tabel,schema=schema) for tabel in gettables(schema)}


if __name__ == '__main__':
    print getTableAndColumns("test")
