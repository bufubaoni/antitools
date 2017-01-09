#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/11/30
from exportexcel import writetoexcel
from info import getTableAndColumns
from verson_name import push_P
from ConfPars import DATABASENAME, NO_NEED_TABLES


class DbExportExcel(object):
    def __init__(self):
        self.Alltables = getTableAndColumns(DATABASENAME)
        pass

    def push_to_verson(self):
        for table in self.Alltables.keys():
            push_P(table)
            for colunm in self.Alltables[table]:
                push_P(colunm[0])

    def export_to_excel(self):
        writetoexcel(tables=self.Alltables)

    def no_need_tables(self, tables=[]):
        for table in tables:
            self.Alltables.pop(table)


if __name__ == '__main__':
    inst = DbExportExcel()
    inst.push_to_verson()
    inst.no_need_tables(tables=NO_NEED_TABLES)
    inst.export_to_excel()
