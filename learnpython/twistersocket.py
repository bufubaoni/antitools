#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/12/12
from twisted.internet import protocol, reactor, endpoints
import cPickle
import struct
import logging
import logging.config

logging.config.fileConfig("logging.conf")
logger = logging.getLogger("server")
logger.setLevel(logging.INFO)


class Echo(protocol.Protocol):
    def __init__(self):
        self._data = ""

    def dataReceived(self, data):
        self._data = self._data.join(data)
        logger.debug(len(self._data))
        self.read()

    def dataunpack(self, data):
        return cPickle.loads(data)

    def datahandler(self, data):
        logger.debug("dataUpanck")
        if len(data) > 4:
            chunk = data[:4]
            slen = struct.unpack('>L', chunk)[0]
            temp = data[len(struct.pack(">L", slen)):len(struct.pack(">L", slen)) + slen]
            logger.debug("slen : {slen}".format(slen=slen))
            self._data = self._data[len(struct.pack(">L", slen)) + slen:]
            self.output(self.dataunpack(temp))

    def read(self):
        while len(self._data) > 4:
            self.datahandler(self._data)

    def output(self, data):
        logger.info(data)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


endpoints.serverFromString(reactor, "tcp:8021").listen(EchoFactory())
reactor.run()
