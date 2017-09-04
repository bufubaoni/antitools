#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/9/1
from requests import Session
import json

session = Session()
url = "https://landray.dingtalkapps.com/alid/reportpc/client/create"

schema = {"atperson": [], "attachmentUri": [], "templateid": "1576b88d2bba77b4b8477934cec8a203", "groupid": "",
          "userid": "", "auths": "", "remark": "", "images": [],
          "detail": [{"key": "今日完成工作", "value": "", "type": "1", "sort": "0"},
                     {"key": "未完成工作", "value": "", "type": "1", "sort": "1"},
                     {"key": "需协调工作", "value": "", "type": "1", "sort": "2"}],
          "isOrgConv": 0, "masterLevels": "",
          "msgMediaId": ""}
header = {
    "Host": "landray.dingtalkapps.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json",
    # "random-numbers": "15045169547111624406",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://landray.dingtalkapps.com/alid/app/reportpc/createreport.html?corpid=dingaeeaf7839044d740&comeFromInside=1",
    "Cookie": "",
    "Connection": "keep-alive"
}


def pub_report(finished="", realtime="", needblame="", userid="01512522161218664"):
    schema["detail"][0]["value"] = finished
    schema["detail"][1]["value"] = realtime
    schema["detail"][2]["value"] = needblame
    schema["userid"] = userid

    session.headers = header

    print session.post(url, data=json.dumps(schema)).text


if __name__ == '__main__':
    pub_report(finished="测试")
