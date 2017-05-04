#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/5/4
from flask import Flask
import argparse

app = Flask(__name__)


@app.route("/")
def hello():
    parser = argparse.ArgumentParser(
        description='Auto-generate a RESTful API service '
                    'from an existing database.'
    )
    parser.add_argument(
        'test',
        help='Database URI in the format '
             'postgresql+psycopg2://user:password@host/database')
    args = parser.parse_args()
    return args.test


if __name__ == "__main__":
    app.run()
