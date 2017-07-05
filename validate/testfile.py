#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cerberus import Validator

schema = {'name': {'type': "string"}}

v = Validator(schema)
if __name__ == '__main__':
    print v.validate({"name": 1})
