#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/3
from db_source import db_s,db_arm

if __name__ == "__main__":
    # db_s.test1.insert(test1="这个", test2="那个")
    # db_s.commit()

    for row in db_s(db_s.test1.test1 != "").iterselect():
        db_arm.test2.insert(test1=row.test1,test3=row.test2,test4=0)
        db_arm.commit()