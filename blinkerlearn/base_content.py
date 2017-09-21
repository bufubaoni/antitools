#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/9/21
import pdb
class Namespace(dict):
    def signal(self,name,doc=None):
        try:
            return self[name]
        except KeyError:
            return self.setdefault(name,"6666666")

if __name__ == '__main__':
    signal = Namespace().signal
    print signal
    pdb.set_trace()