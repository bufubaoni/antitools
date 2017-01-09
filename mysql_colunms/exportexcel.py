#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/11/30
import xlsxwriter
from verson_name import get_P

from ConfPars import OUTPUT_EXCEL


def workbookexcel(name="test"):
    def action(excel):
        def openexcel(*args, **kwargs):
            workbook = xlsxwriter.Workbook(name)
            worksheet = workbook.add_worksheet()
            result = excel(worksheet=worksheet, *args, **kwargs)
            workbook.close()
            return result

        return openexcel

    return action


@workbookexcel(name=OUTPUT_EXCEL)
def writetoexcel(worksheet=None, tables=None):
    start = 1
    if isinstance(tables, dict):
        for tabname, table in tables.items():
            exporttable(worksheet, {tabname: table}, start)
            start += len(table)
            start += 1


def exporttable(worksheet=None, table=None, start=None):
    tablename = table.keys()[0]
    worksheet.write("A" + str(start), tablename)
    worksheet.write("A" + str(start + 1), get_P(tablename))
    for row, culonm in enumerate(table[tablename]):
        print culonm
        worksheet.write("B" + str(row + start), culonm[0])
        worksheet.write("C" + str(row + start), culonm[3].decode("utf8"))
        worksheet.write("D" + str(row + start), culonm[1])
        worksheet.write("E" + str(row + start), get_P(culonm[0]))


if __name__ == '__main__':
    table = {'car_customer': [('id', 'NO', 'int', 'int(11)'),
                              ('uuid', 'YES', 'varchar', 'varchar(32)'),
                              ('car', 'YES', 'varchar', 'varchar(32)'),
                              ('customer', 'YES', 'varchar', 'varchar(20)'),
                              ('createby', 'YES', 'int', 'int(11)'),
                              ('createon', 'YES', 'datetime', 'datetime'),
                              ('modifyby', 'YES', 'int', 'int(11)'),
                              ('modifyon', 'YES', 'datetime', 'datetime')],
             }

    writetoexcel(tables=table)
