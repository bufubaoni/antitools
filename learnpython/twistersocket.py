#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/12/12
from twisted.internet import protocol, reactor, endpoints
import cPickle
import struct


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        data = self.dataUnpack(data=data)
        print data

    def dataUnpack(self, data):
        chunk = data[:4]
        slen = struct.unpack('>L', chunk)[0]
        data = data[len(struct.pack(">L", slen)):]
        return cPickle.loads(data)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


endpoints.serverFromString(reactor, "tcp:8020").listen(EchoFactory())
reactor.run()
