#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/8/8
from celery.app import Celery
app = Celery("celery_test",broker="amqp://alex:123456@192.168.85.130:5672/",backend="amqp")
# app.connection("192.168.85.130")

@app.task
def add(x,y):
    return x+y
#
if __name__ == '__main__':
    app.start()
    print app.__dict__