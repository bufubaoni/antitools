#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/8/18
from celery_test import add
# print type(add)
add.delay(124, 11112)
# print a
# print add.AsyncResult(a).ready()
# print a.get()

from base64 import b64decode
import pickle
#
print pickle.loads(b64decode(
    "gAJ9cQEoVQZzdGF0dXNxAlUHU1VDQ0VTU3EDVQl0cmFjZWJhY2txBE5VBnJlc3VsdHEFTeMrVQd0YXNrX2lkcQZVJDY2MTZhNGQwLWIxODEtNDY1MS1hNzMzLWEyNzBkMmMyYTkzNHEHVQhjaGlsZHJlbnEIXXUu"))

print add.AsyncResult(task_id="e2524bcc-10c3-4906-bdec-f98bdff8d70b").state
