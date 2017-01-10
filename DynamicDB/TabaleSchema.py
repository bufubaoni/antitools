#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/10
from pydal import DAL, Field


def get_sys_table(uri="mysql://lms_test:lmsadmin@192.168.1.110/information_schema"):
    sys_tab = DAL(uri=uri)

    sys_tab.define_table('COLUMNS',
                         Field("TABLE_SCHEMA", ),
                         Field("TABLE_NAME"),
                         Field("COLUMN_NAME"),
                         Field("IS_NULLABLE"),
                         Field("DATA_TYPE"),
                         Field("COLUMN_TYPE"),
                         primarykey=[],
                         migrate=False)
    return sys_tab


def datatype_mysql():
    return dict(
        varchar='string',
        int='integer',
        integer='integer',
        tinyint='integer',
        smallint='integer',
        mediumint='integer',
        bigint='integer',
        float='double',
        double='double',
        char='string',
        decimal='integer',
        date='date',
        time='time',
        timestamp='datetime',
        datetime='datetime',
        binary='blob',
        blob='blob',
        tinyblob='blob',
        mediumblob='blob',
        longblob='blob',
        text='text',
        tinytext='text',
        mediumtext='text',
        longtext='text',
    )
