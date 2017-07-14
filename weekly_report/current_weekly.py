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


class WeeklyReportTime(object):
    def __init__(self, delay=0, formate="%m.%d"):
        self._format = formate
        self._day = datetime.now()
        self.current_time = begin_end_week_day(self._day, delay)

    def __str__(self):
        return "{0}~{1}".format(self.current_time[0].strftime(self._format),
                                self.current_time[1].strftime(self._format))


if __name__ == '__main__':
    # print calendar.weekday(current_day.year, current_day.month, current_day.day)
    print begin_end_week_day(current_day)
    print WeeklyReportTime(1)
