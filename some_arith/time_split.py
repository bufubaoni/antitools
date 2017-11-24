#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/11/24
from datetime import timedelta, datetime


def time_split(seconds=60):
    def wrap(fun):
        def proxy(start, end):
            list_span = range(0, int((end - start).total_seconds() / seconds))
            l_time_group = list()
            for item in list_span:
                l_time_group.append(
                     [start + timedelta(seconds=seconds * item), start + timedelta(seconds=seconds * (item+1))])
            else:
                l_time_group[-1][1] = end

            result = list()

            for item in l_time_group:
                print
                result.extend(fun(*item))
            return result

        return proxy

    return wrap


@time_split(seconds=60)
def fun(start, end):
    print start
    print end
    return range(0, (end - start).seconds)


if __name__ == '__main__':
    print fun(datetime.now(), datetime.now() + timedelta(seconds=121))
