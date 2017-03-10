#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/9/18

def task_log(task):
    print(1)
    def decorator(*a, **k):
        return task(*a, **k)
    return decorator

def task_log_para(para):
    print(para)
    def wrapping(task):
        def decorator(*a,**k):
            return task(*a,**k)
        return decorator
    return wrapping


@task_log
@task_log_para("para 1")
def test(a):
    print(a)
    return a


if __name__ == '__main__':
    test("asdffff")
