#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/12/12
from twisted.internet import protocol, reactor, endpoints
import cPickle
import struct
import logging
import logging.config
import time

logging.config.fileConfig("logging.conf")
logger = logging.getLogger("server")
logger.setLevel(logging.INFO)

class Echo(protocol.Protocol):
    def __init__(self):
        self._data = ""

    def dataReceived(self, data):
        # data = self.dataUnpack(data=data)
        logger.debug("ok")
        # self.transport.write("ok")
        logger.debug(len(data))
        self._data += data
        if len(self._data) > 4:
            logger.debug("6")
            self.dataUnpack(self._data)
        else:
            logger.debug(len(self._data))

    def dataUnpack(self, data):

        logger.debug("dataUpanck")
        chunk = data[:4]
        slen = struct.unpack('>L', chunk)[0]
        temp = data[len(struct.pack(">L", slen)):len(struct.pack(">L", slen)) + slen]
        logger.debug("slen : {slen}".format(slen=slen))
        self._data = self._data[len(struct.pack(">L", slen)) + slen:]
        if len(self._data) > 4:
            self.dataUnpack(self._data)
        print(cPickle.loads(temp))

        # def dataHandler(self,data):


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


endpoints.serverFromString(reactor, "tcp:8021").listen(EchoFactory())
reactor.run()
