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
            for key, value in request.data.items():
                setattr(Para, key, value)
            Result = namedtuple("result", result.keys())
            return task(cls, request, Para, Result, *_args, **k)
        return decorator
    return wrapping


@restful({"username": "str",
          "password": "str"},
         {"result": "star"})
def test(self, request, para, result):
    print self
    print request
    # para.username = "fuck"
    # para.password = "1234546"
    # print dir(para)
    print dir(result)
    print para._asdict
    print para.username


if __name__ == "__main__":
    test("self", {"username": "username", "password": "password"})


