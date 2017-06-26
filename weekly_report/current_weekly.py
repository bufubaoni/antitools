#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/6/26
from datetime import datetime, timedelta
import calendar
import pdb

current_day = datetime.now()


def begin_end_week_day(current_day, delay=0):
    begin = (datetime.now() - timedelta(days=current_day.weekday())) + timedelta(days=7 * delay)
    end = begin + timedelta(days=4)
    return begin, end


if __name__ == '__main__':
    # print calendar.weekday(current_day.year, current_day.month, current_day.day)
    print begin_end_week_day(current_day)
