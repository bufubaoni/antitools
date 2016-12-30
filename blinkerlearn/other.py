#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/12/30
from blinker import signal

test_message = signal("test")


@test_message.connect
def test(sender):
    print ("other module {sender}".format(sender=sender))
