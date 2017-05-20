#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/5/15
from websocket import create_connection
print "faulttest"
localhost = True
if localhost:
    ws_uri = "ws://127.0.0.1:8888/websocket"
else:
    ws_uri = "ws://172.16.15.205:18089/web/v3/fault_alarm_websocket/"

# ws_uri = "ws://127.0.0.1:9001/web/v3/fault_alarm_websocket/"
# #
# #
# for i in range(100):
#     print i
ws = create_connection(ws_uri)
import time
while True:
    # ws.send("ok")
    print ws.recv()
    time.sleep(1)