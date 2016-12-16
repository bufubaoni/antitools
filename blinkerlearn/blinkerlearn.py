#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/12/16
# e.g.1
from blinker import signal, Signal

initialized = signal("initialized")


# e.g.2
def subscriber(sender):
    print('Got a signal sent by {sender}'.format(sender=sender))


# e.g.3
class Processor(object):
    def __init__(self, name):
        self.name = name

    def go(self):
        ready = signal('ready')
        ready.send(self)
        print('Processing.')
        complete = signal('complete')
        complete.send(self)

    def __repr__(self):
        return "<Processor {name}>".format(name=self.name)


# e.g.4
def b_subscriber(sender):
    print('Caught signal form processor_b.')
    assert sender.name == 'b'


# e.g.5
send_data = signal('send-data')


@send_data.connect
def receive_data(sender, **kw):
    print ("Caught signal form {sender}, data {data}".format(sender=sender, data=kw))
    return 'received!'


# e.g.6
class AltProcessor(object):
    on_ready = Signal()
    on_complete = Signal()

    def __init__(self, name):
        self.name = name

    def go(self):
        self.on_ready.send(self)
        print("Alternate processing.")
        self.on_complete.send(self)

    def __repr__(self):
        return '<AltProcessor {name}>'.format(name=self.name)


apc = AltProcessor("c")


@apc.on_complete.connect
def completed(sender):
    print ("AltProcessor {sender} completed!".format(sender=sender.name))


# e.g.7
dice_roll = signal('dice_roll')


@dice_roll.connect_via(1)
@dice_roll.connect_via(3)
@dice_roll.connect_via(5)
def odd_subscriber(sender):
    print ('Observed dice roll {sender}'.format(sender=sender))


if __name__ == '__main__':
    # e.g.1
    print(initialized is signal('initialized'))
    # e.g.2
    ready = signal('ready')
    print(ready.connect(subscriber))
    # e.g.3
    processor_a = Processor('a')
    processor_a.go()
    # e.g.4
    processor_b = Processor('b')
    ready.connect(b_subscriber, sender=processor_b)
    processor_b.go()
    # e.g.5
    result = send_data.send("anonymous", abc=123)
    print (result)
    # e.g.6
    apc.go()
    # e.g.7
    result = dice_roll.send(3)
    # e.g.8
    print (bool(signal('ready').receivers))
    print (bool(signal('complete').receivers))
    print (bool(AltProcessor.on_complete.receivers))

    print(bool(signal('ready').has_receivers_for(processor_a)))
