# -*- coding: utf-8 -*-
import os


def addfile(file_name):
    cmd = 'git add {}'.format(file_name)
    os.popen(cmd)


def commit():
    cmd = "git commit"
    os.popen(cmd)


def last_cmt_amend_date(date):
    cmd = 'git commit --amend --date="{}"'.format(date)
    os.popen(cmd)


def fackaddfile(file_name, date):
    addfile(file_name)
    commit()
    last_cmt_amend_date(date)


if __name__ == "__main__":
    fackaddfile('git_commit/cmtgit.py', "2020-03-29 11:40:30")
