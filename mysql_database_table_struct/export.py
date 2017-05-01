#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/4/6
from mysql_model import sys_tab
from ConfPars import TABLES, SCHEMA, OUTPUT_FILE
import json


def gettables(schema):
    return {table: getcolumns(table, schema) for table in TABLES}


def getcolumns(table, schema):
    columns = sys_tab((sys_tab.COLUMNS.TABLE_NAME == table) & (sys_tab.COLUMNS.TABLE_SCHEMA == schema)). \
        select(sys_tab.COLUMNS.COLUMN_NAME,
               sys_tab.COLUMNS.IS_NULLABLE,
               sys_tab.COLUMNS.DATA_TYPE,
               sys_tab.COLUMNS.COLUMN_TYPE,
               sys_tab.COLUMNS.TABLE_SCHEMA)
    columns = {column.COLUMN_NAME: column.DATA_TYPE for column in columns if column.IS_NULLABLE=="NO"}
    if "id" in columns:
        columns.pop("id")

    return columns


def export(content):
    with open(OUTPUT_FILE, "a") as f:
        f.write(content)


def main():
    schema = SCHEMA
    export(json.dumps(gettables(schema)))


if __name__ == "__main__":
    main()
