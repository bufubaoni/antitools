#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/10
from pydal import DAL, Field
from AllTables import GetAllTables


class DyTables(object):
    def __init__(self, uri=None):
        self._uri = uri
        self._schema = uri.split("/")[-1]
        self._dal = DAL(self._uri)
        self.get_tables()

    def get_tables(self):
        _tables = GetAllTables(schema=self._schema)
        for numb, table in enumerate(_tables):
            fields = []
            for field in _tables.get(table):
                fields.append(Field(field[0]))
            self._dal.define_table(table, *fields, primarykey=[], migrate=False)

    def get_db(self):
        return self._dal


if __name__ == '__main__':
    dtb = DyTables(uri='mysql://lms_test:lmsadmin@192.168.1.110/lms_test').get_db()
    print dtb(dtb.car.id > 0).select()
