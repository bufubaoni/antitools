#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/12/28
import logging
import logging.config
from celery import Celery
from SaveFile import save_file, basedir

basedir = "D:/downloads/"

app = Celery()


@app.task
def save_task(pin, basedir=basedir):
    save_file(pin, basedir=basedir)


logging.config.fileConfig("logging.conf")
logger = logging.getLogger("scheduler")

if __name__ == '__main__':
    app.worker_main()
