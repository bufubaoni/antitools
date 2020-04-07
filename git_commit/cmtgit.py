# -*- coding: utf-8 -*-
import os


def addfile(file_name):
    cmd = 'git add {}'.format(file_name)
    os.popen(cmd)


def commit(file_name):
    cmd = "git commit -m 'add {}'".format(os.path.basename(file_name))
    os.popen(cmd)


def last_cmt_amend_date(date):
    cmd = 'git commit --amend --no-edit --date="{}"'.format(date)
    os.popen(cmd)


def fackaddfile(file_name, date):
    addfile(file_name)
    commit(file_name)
    last_cmt_amend_date(date)


if __name__ == "__main__":
    fackaddfile('cmtgit.py', "2020-03-28 11:40:30")
