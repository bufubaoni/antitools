#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/12/28
import logging
import logging.config
import json

logging.config.fileConfig("logging.conf")
logger = logging.getLogger("pars")


def pars(content):
    board = dict()
    for line in content:
        # logger.debug(line)
        board = app_board(line)
        if board:
            board = json_board(board)
            break
    return board

def app_board(line):
    if 'app.page["board"]' in line:
        logger.debug("=============board===========")
        logger.debug(line)
        return line
    else:
        return None


def json_board(app_board_line):

    temp_board = app_board_line.split("=")[1]
    logger.debug(temp_board)

    # logger.debug(json_b)
    # return json_b

if __name__ == '__main__':
    with open("page.html", "r") as f:
        content = f.readlines()
        pars(content)
