#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/6/12
from requests import Session
import sys
from pykafka import KafkaClient
from pykafka.exceptions import SocketDisconnectedError
import logging
import pdb
import getopt
from datetime import datetime

# topic
# topic_fault
# topic_water
# topic_other_warnning
#
# topic_alarm

# request_addr


sub_addr, topic, request_addr, consumer_id = "", "", "",""

# logger
FORMATER = '%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMATER)
logger = logging.getLogger(topic)
logger.setLevel(logging.DEBUG)

# consumer group id
group_id = '80f0cfcf-4b28-11e7-a3e3-005056c00008'

session = Session()


def get_agrs():
    opts, _ = getopt.getopt(sys.argv[1:], "h:t:u:c")
    return opts


args = get_agrs()

if args:
    for opt, value in args:
        if opt == "-h":
            sub_addr = value
        elif opt == "-t":
            topic = value
        elif opt == "-u":
            request_addr = value
        elif opt == "-c":
            consumer_id = value


def _send(request_addr, message):
    return session.post(request_addr, data=message)
    # logger.info(request_addr, message)


def loops():
    logger.info(sub_addr)
    logger.info(topic)
    logger.info(request_addr)
    client_msg = KafkaClient(hosts=sub_addr)
    topic_fault = client_msg.topics[topic]
    consumer = topic_fault.get_simple_consumer(consumer_group=group_id, auto_commit_enable=True,
                                               auto_commit_interval_ms=1, consumer_id=consumer_id)
    logger.info("==========={topic}_consumer_run=================".format(topic=topic))
    while True:
        try:
            for message in consumer:
                if message.value:
                    logger.info("{topic}_consumer--->{message}".format(topic=topic, message=message.value))
                    _send(request_addr, message.value)

        except SocketDisconnectedError as e:
            consumer = topic_fault.get_simple_consumer(consumer_group=group_id, auto_commit_enable=True,
                                                       auto_commit_interval_ms=1, consumer_id=consumer_id)
            logger.error("{topic}_connect_again.....".format(topic=topic))

        logger.debug("{topic}_loop_run".format(topic=topic))


if __name__ == "__main__":
    # print get_agrs()
    loops()
