#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/8/8
from celery.app import Celery
app = Celery("test",broker="amqp://alex:123456@192.168.85.130:5672/")
# app.connection("192.168.85.130")

@app.task
def add(x,y):
    return x+y
#
if __name__ == '__main__':
    app.worker_main()