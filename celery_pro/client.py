#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/8/18
from celery_test import add

print add.delay(12,13).get()