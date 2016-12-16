#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/12/16

from blinker import signal

test_message = signal("test")


@test_message.connect
def test_a(sender):
    print("this is test a by sender: {sender}".format(sender=sender))


@test_message.connect
def test_b(sender):
    print("this is test b by sender: {sender}".format(sender=sender))

test_message.send("haha")