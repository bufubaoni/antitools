#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/3/23


class JsonDict(dict):
    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError(r"'JsonDict' objectg has no attribute '%s'" % attr)

    def __setattr__(self, attr, value):
        self[attr] = value


class JsonDictSimple(dict):
    """
    set attr like obj
    """
    __setattr__ = dict.__setitem__

    def __getattr__(self, name):
        value = self.get(name)
        if isinstance(value, dict):
            return JsonDictSimple(value)
        else:
            return value


if __name__ == "__main__":
    j = JsonDict({"a": 1, "b": 2, "c": ["q5"]})
    j.c.append("qq")
    d = JsonDictSimple()
    d.a = 666
    d = JsonDictSimple({"a": 1, "b": {"c": "q5"}})
    print d.a
    print j, d
    print d.b.c
