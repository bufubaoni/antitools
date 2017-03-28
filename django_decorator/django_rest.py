#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/3/23
from collections import namedtuple


def restful(para, result):
    def wrapping(task):
        def decorator(*a, **k):
            _args = list(a)
            cls = _args.pop(0)
            request = _args.pop(0)

            paras = JsonDict(**para)

            results = JsonDict(**result)

            info = JsonDict({"msg": "",
                             "status": -1})

            return task(cls, request, paras, results, info, *_args, **k)

        return decorator

    return wrapping


class JsonDict(dict):
    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError(r"'JsonDict' objectg has no attribute '%s'" % attr)

    def __setattr__(self, attr, value):
        self[attr] = value


@restful({"username": "",
          "password": ""},
         {"result": ""})
def test(self, request, para, result, info):
    print self
    print request
    print dir(result)
    print info
    import json
    print json.dumps(para)
    print para.username


if __name__ == "__main__":
    test("self", {"username": "username", "password": "password"})
