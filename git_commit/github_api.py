# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import random
import json
import os
from cmtgit import fackaddfile
BEGIN = "2019-03-31"

END = "2020-03-31"
FORM = '%Y-%m-%d'
EXCLUDES = []


def get_json(filename):
    f = open(filename, 'r')
    sj = ''.join(f.readlines())
    f.close()
    return json.loads(sj)


def dumps(lst, filename):
    f = open(filename, 'w')
    lst = json.dumps(lst)
    f.write(lst)
    f.close()


def get_radom(a, b):
    return str(random.randint(a, b)).zfill(2)


def generate_timeline(excludes):
    begin = datetime.strptime(BEGIN, FORM)
    end = datetime.strptime(END, FORM)

    timeline = []
    while begin < end:
        if begin.isoweekday() not in [6, 7] and begin.strftime(FORM) not in excludes:
            timeline.append(begin.strftime(FORM))
        begin = timedelta(days=1) + begin
    return timeline


def get_files(path, excludes_files):
    file = files(path)
    for base, dr, fs in file:
        if base == path:
            for f in fs:
                if f not in excludes_files:
                    yield base + "/" + f


def files(path):
    files = os.walk(path)
    return list(files)


def m():
    excluese_times = get_json('git_commit/timecmt.json')
    times = generate_timeline(excluese_times)

    excluese_file = get_json('git_commit/ex_file.json')
    idx = 0
    for file in get_files('/Users/chenxin/tools/algorithms', excluese_file):

        excluese_file.append(os.basename(file))
        time = times[idx]
        fackaddfile(file, time+' {}:{}:{}'.format(get_radom(8, 20), get_radom(0, 60), get_radom(0, 60)))
        excluese_times.append(time)
        idx += 1

    dumps(excluese_times, 'base.json')
    dumps(excluese_file, 'ex_files.json')


if __name__ == "__main__":
    # excluese = get_json('git_commit/timecmt.json')
    # dumps(excluese, 'git_commit/base.json')

    # print files('tools')
    # print list(get_files('/Users/chenxin/tools/algorithms', ["README.md"]))
    # dumps
    # print generate_timeline(excluese)
    m()
