#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/12/9
import logging
import logging.config
logging.config.fileConfig("logging.conf")
logger = logging.getLogger("test")
logger.setLevel(logging.DEBUG)



if __name__ == "__main__":
    logger.debug("testddd")
    logger.warn("warning")
    # logger.info("yes")
    # try:
    #     str.qq
    # except Exception as e:
    #     logger.exception(e)