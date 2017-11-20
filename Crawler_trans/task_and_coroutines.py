#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/11/20
from gevent import Greenlet
import gevent

class MyNoopGreenlet(Greenlet):
    def __init__(self, seconds):
        Greenlet.__init__(self)
        self.seconds = seconds

    def _run(self):
        print "run server"
        gevent.sleep(self.seconds)

    def __str__(self):
        return 'MyNoopGreenlet(%s)' % self.seconds


from gevent.hub import Waiter,get_hub

result = Waiter()

timer = get_hub().loop.timer(1)

import gevent
import signal

def run_forever():
    while True:
        print "run start"
        gevent.sleep(1)
        print "run stop"

def something():
    while True:
        print "other process run"
        gevent.sleep(1)
    # print "other process run"
if __name__ == '__main__':
    gevent.signal(signal.SIG_IGN, gevent.kill)
    thread = gevent.spawn(run_forever)
    thread.spawn(something)
    thread.join()

# if __name__ == '__main__':
#     timer.start(result.switch, "hello from waiter")
#     print result.get()