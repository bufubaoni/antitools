#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/11/21
from celery.signals import after_task_publish


@after_task_publish.connect(sender="celery_pro.celery_test.add")
def task_send_handler(sender=None,body=None,**kwargs):
    print kwargs
    print sender
    print body
    print ('after_task_publis for task21233333123')