#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/9/5
import requests
from requests.auth import HTTPBasicAuth
import sys

session = requests.Session()
res = session.get(('http://192.168.1.109:9001/?'
                   'processname={task_name}&amp;'
                   'action={task_action}'.format(task_name=sys.argv[1],
                                                 task_action=sys.argv[2])),
                   auth=HTTPBasicAuth('username', 'password'))

