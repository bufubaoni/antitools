#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/11/22
from __future__ import print_function
import sys
from gevent import socket
import json

address = ('localhost', 9000)
message = ' '.join(sys.argv[1:])
sock = socket.socket(type=socket.SOCK_DGRAM)
sock.connect(address)
sock.send(json.dumps({"module": "task_test",
              "method": "test_task"}))
data, address = sock.recvfrom(8192)
