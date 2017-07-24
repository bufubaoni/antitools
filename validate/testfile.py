#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cerberus import Validator

schema = {'name': {'type': "string", 'regex': "[0-9]+"},
          "password": {'type': "string", 'regex': "[0-9a-zA-Z]{6:20}", "empty": False, 'nullable': False,
                       'required': True}}

v = Validator(schema)
if __name__ == '__main__':
    if not v.validate({"name": u"1"}):
        print v.errors
    else:
        print "ok"
