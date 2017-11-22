#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/8/8
from celery.app import Celery

app = Celery("celery_test", broker="redis://127.0.0.1:6379/0", backend="redis")
# app.connection("192.168.85.130")
from celery.signals import after_task_publish


@app.task
def add(x, y):
    return x + y


@after_task_publish.connect
def task_send_handler(sender=None, body=None, **kwargs):
    print kwargs
    print sender
    print body
    print ('after_task_publis for task')


    # if __name__ == '__main__':
    #     app.start()
