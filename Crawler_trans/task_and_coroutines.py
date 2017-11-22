#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/11/20
from gevent import Greenlet
import gevent

task_list = list()


class MyNoopGreenlet(Greenlet):
    def __init__(self, seconds):
        Greenlet.__init__(self)
        self.seconds = seconds

    def _run(self):
        print "run server"
        gevent.sleep(self.seconds)

    def __str__(self):
        return 'MyNoopGreenlet(%s)' % self.seconds


from gevent.hub import Waiter, get_hub

result = Waiter()

timer = get_hub().loop.timer(1)

import gevent
import signal


def run_forever():
    print id(task_list)
    while True:
        print "heart beat"
        gevent.sleep(1)
        if len(task_list):
            task = task_list.pop()
            if callable(task):
                task()


if __name__ == '__main__':
    thread = gevent.spawn(run_forever)
    thread.join()
