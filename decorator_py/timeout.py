# -*- coding: utf-8 -*-
from gevent import monkey
monkey.patch_all()  # noqa
import time
import timeout_decorator


class MyError(Exception):
    pass


@timeout_decorator.timeout(5, timeout_exception=MyError, use_signals=False)
def mytest(q):
    print "Start"
    for i in range(1, 10):
        time.sleep(1)
        print "%d seconds have passed" % i


if __name__ == '__main__':
    mytest(2)
