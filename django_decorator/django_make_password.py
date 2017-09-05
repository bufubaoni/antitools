#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/9/5
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_decorator.settings")
from django.contrib.auth.hashers import make_password

if __name__ == '__main__':
    pass
    print make_password("qttc", None, 'pbkdf2_sha256')
