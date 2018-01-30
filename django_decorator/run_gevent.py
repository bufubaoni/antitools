#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gevent import monkey

monkey.patch_all()  # noqa
from gevent.wsgi import WSGIServer

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xxx.settings")

application = get_wsgi_application()
server = WSGIServer(("0.0.0.0", 9001), application)
print "Starting server on http://127.0.0.1:9001"
server.serve_forever()
