#!/usr/bin/env python
# -*- coding: utf-8 -*-
from prettytable import PrettyTable

def json2report(content,savepath):
    table = PrettyTable()
    table.field_names = content['06.27-06.30'][0].keys()
    table.add_row(content['06.27-06.30'][0].values())
    print table

if __name__ == '__main__':
    import json
    with open("test_report_simple.json",'r') as report:
        s = "".join(report.readlines())
        print s
        rep = json.loads(s, "utf8")
        json2report(rep,None)
