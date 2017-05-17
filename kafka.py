#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/5/17
from pykafka import KafkaClient
import time
print time.time()
client_msg = KafkaClient(hosts="xxx.xxx.x.x:xxxx")
print time.time()
topic_fault = client_msg.topics['xxx']
print time.time()
consumer_fault = [(topic_fault.get_simple_consumer(consumer_group='con_1', auto_commit_enable=True,
                                                   auto_commit_interval_ms=1, consumer_id='sec2'))]
print time.time()