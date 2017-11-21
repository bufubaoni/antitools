#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/11/21
from celery_pro.celery_test import add

if __name__ == '__main__':
    add.delay(x=4,y=1)