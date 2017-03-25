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

if __name__ == "__main__":
    j = JsonDict({"a":1,"b":2})
    print j
