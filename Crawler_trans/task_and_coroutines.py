#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/11/20
from gevent import monkey
monkey.patch_all()
import gevent
from gevent import socket
task_list = list()


def run_forever():
    while True:
        print "heart beat"
        gevent.sleep(1)
        if len(task_list):
            task = task_list.pop()
            if callable(task):
                task()


def add_tasks(module, name):
    _class = __import__(module)
    method = getattr(_class, name)
    task_list.append(method)


from gevent.server import DatagramServer
import json


class EchoServer(DatagramServer):

    def handle(self, data, address):
        if data:
            data = json.loads(data)
            add_tasks(data["module"], data["method"])


def share_task(fun):
    def w(*a, **k):

        if fun.func_globals["__name__"] == "__main__":
            address = ('localhost', 9000)
            message = {"module": fun.func_globals["__file__"].split("/")[-1].split(".")[0],
                       "method": fun.__name__}
            sock = socket.socket(type=socket.SOCK_DGRAM)
            sock.connect(address)
            sock.send(json.dumps(message))
        return fun(*a, **k)
    return w


def wait_add_tasks():
    pass


if __name__ == '__main__':
    thread = gevent.spawn(run_forever)
    EchoServer(':9000').serve_forever()
    thread.join()
