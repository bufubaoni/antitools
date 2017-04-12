#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/3/23
from collections import namedtuple
import re
import pdb
def restful(para, result):
    def wrapping(task):
        def decorator(*a, **k):
            _args = list(a)
            cls = _args.pop(0)
            request = _args.pop(0)

            paras = JsonDict(**para)

            results = JsonDict(**result)

            irregular = []
            for key, value in request.items():
                if not re.match(para.get(key),request.get(key)):
                    irregular.append(key)
            print irregular

            paras.update(**request)
            info = JsonDict({"msg": "",
                             "status": -1})

            return task(cls, request, paras, results, info, *_args, **k)

        return decorator

    return wrapping


class RField(object):
    def __init__(self, field_name, verbose_name=None, field_type="str", null=True, blank=True, validators=None):
        self._field_name = field_name,
        self._verbose_name = verbose_name if verbose_name else field_name
        self._field_type = field_type
        self._null = null
        self._blank = blank
        self._validators = validators

        self._value = None
        self._convert = {"str": str,
                         "int": int}

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value

    @property
    def value(self):
        return self._convert[self._field_type](self._value)

    @value.setter
    def value(self, value):
        print 1
        if not self._validators:
            self._value = value
        else:
            if self._validators(value):
                self._value = value
            else:
                raise ValueError("%s value error", self._field_name)


class JsonDict(dict):
    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError(r"'JsonDict' objectg has no attribute '%s'" % attr)

    def __setattr__(self, attr, value):
        self[attr] = value


@restful({"username": "[a-z].",
          "password": "^[a-z]+$"},
         {"result": ""})
def test(self, request, para, result, info):
    print para.username
    print para.username


class Test(object):
    pass


# class Route()
routes = {}


def route(table, method):
    # routes = {}

    def wrapping(task):
        routes[table + "_" + method] = task

        def decorator(*a, **k):
            return task(*a, **k)

        return decorator

    return wrapping


@route("rt_date", "insert")
def test1():
    print 1
    pass


@route("rt_date", "update")
def test2():
    print 2
    pass


if __name__ == "__main__":
    # routes["rt_date_insert"]()
    # routes["rt_date_update"]()
    test("self", {"username": "username1", "password": "passwsord"})
# t = Test()
# t.good = 10
# t.username = 100
# print t.username
