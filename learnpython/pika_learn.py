#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/8/18
import pika
from pika.credentials import PlainCredentials,ExternalCredentials
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.85.130',credentials=PlainCredentials("alex","123456")),)
channel = connection.channel()

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello Worldccccccc!')