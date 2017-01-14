#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/12/28
import logging
import logging.config
import json

logging.config.fileConfig("logging.conf")
logger = logging.getLogger("pars")


def pars(content):
    '''
    splite content and find app board from html.

    Returns app board json str

    Args:
        content: www.huaban.com format html
    '''
    board = dict()
    logger.debug(content)
    content = content.split("\n")
    for line in content:
        board = app_board(line)
        if board:
            board = json_board(board)
            break
    return board


def app_board(line):
    """
    find board line from html content

    Returns app board str

    Args:
        line: content line
    """
    if 'app.page["board"]' in line:
        logger.debug(line)
        return line
    else:
        return None


def json_board(app_board_line):
    """
    from board json str convert dict

    Returns app board dict

    Args:
        app_board_line:json str
    """
    temp_board = "".join(app_board_line.split("=")[1:])
    logger.debug(temp_board.strip()[:-1])
    json_b = json.loads(temp_board.strip()[:-1])
    logger.debug("==============decode json================")
    return json_b


if __name__ == '__main__':
    with open("page.html", "r") as f:
        content = f.readlines()
        pars("".join(content))
