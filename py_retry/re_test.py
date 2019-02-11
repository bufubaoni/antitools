# -*- coding: utf-8 -*-

from retrying import retry, RetryError
import logging


class TestError(Exception):
    pass


def retry_if_io_error(exception):
    logging.warning(exception)
    return isinstance(exception, TestError)


@retry(retry_on_exception=retry_if_io_error,
       stop_max_attempt_number=3,
       wait_exponential_multiplier=10)
def test():
    raise TestError('test error')


if __name__ == "__main__":
    try:
        test()
    except RetryError as e:
        logging.exception('retry error')
    except TestError as e:
        logging.error('test error')
    except Exception as e:
        print "--------========--------"
        logging.exception(e)
