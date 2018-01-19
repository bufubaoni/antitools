#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/8/29


def inc(x):
    return x + 1


def function_dir(methods=None, **kwargs):
    """
    Used to mark a method on a ViewSet that should be routed for list requests.
    """
    methods = ['get'] if (methods is None) else methods

    def decorator(func):
        func.bind_to_methods = methods
        func.detail = False
        func.kwargs = kwargs
        return func
    return decorator


def test_answer():
    assert inc(5) == 5


class A(object):
    def __init__(self):
        self.x = 'ccccc'

    @function_dir(method=['post'])
    def get_x(self):

        import pdb
        pdb.set_trace()
        return self.x


if __name__ == "__main__":
    a = A()
    print a.get_x()
    print a.get_x
    print inc
