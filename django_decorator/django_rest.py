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

            Para = namedtuple("para", para.keys())
            paras = Para(**request.data)

            Result = namedtuple("result", result.keys())
            results = Result(**result)

            Info = namedtuple("Info", ["msg", "status"])
            info = Info("", -1)

            return task(cls, request, paras, results, info, *_args, **k)

        return decorator

    return wrapping


@restful({"username": "",
          "password": ""},
         {"result": ""})
def test(self, request, para, result, info):
    print self
    print request
    # para.username = "fuck"
    # para.password = "1234546"
    # print dir(para)
    print dir(result)
    print info
    import json
    print json.dumps(para._asdict())
    print para.username


if __name__ == "__main__":
    test("self", {"username": "username", "password": "password"})
