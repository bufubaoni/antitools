import time
import timeout_decorator


class MyError(Exception):
    pass


@timeout_decorator.timeout(5, timeout_exception=MyError)
def mytest():
    print "Start"
    for i in range(1, 10):
        time.sleep(1)
        print "%d seconds have passed" % i


if __name__ == '__main__':
    mytest()
