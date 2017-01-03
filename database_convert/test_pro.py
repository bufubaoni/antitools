#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/3
from db_source import db_s

if __name__ == "__main__":
    db_s.test1.insert(test1="这个", test2="那个")
