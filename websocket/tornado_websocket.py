#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/5/15
import tornado.ioloop
import tornado.web
import tornado.websocket
import time
from datetime import datetime


class MainHandler(tornado.websocket.WebSocketHandler):
    # CLOSED = False
    Clients = []

    def open(self):
        self.tm = datetime.now()
        self.CLOSED = False
        msg_num = 0

        # while not self.CLOSED and (datetime.now() - self.tm).total_seconds() < 20:
        #     msg_num += 1
        #     msg = "%s fault" % msg_num
        #     self.write_message(msg)
        #     print msg
        #     time.sleep(5)
        print("WebSocket opened")

    def on_message(self, message):
        #
        # while not self.CLOSED:
        #     msg_num +=1
        #     self.write_message("%s fault" % msg_num)
        #     time.sleep(5)
        self.write_message(u"You said: " + message)

    def on_close(self):
        self.CLOSED = True
        print("WebSocket closed")


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/websocket", MainHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
