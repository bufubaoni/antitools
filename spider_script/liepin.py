#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/11
from requests import Session

import md5

passwd = "passwod"
username = "username"

mpass = md5.new()
mpass.update(passwd)
passwd = mpass.hexdigest()

session = Session()
headers = {'Host': 'passport.liepin.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
           'Accept': 'application/json, text/javascript, */*; q=0.01',
           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
           'Accept-Encoding': 'gzip, deflate, br',
           'Content-Type': 'application/x-www-form-urlencoded',
           'X-Alt-Referer': 'https://www.liepin.com/',
           'X-Requested-With': 'XMLHttpRequest',
           'Referer': 'https://passport.liepin.com/ajaxproxy.html',
           'Content-Length': '117',
           'Cookie': '',
           'Connection': 'keep-alive'
           }


content = session.post("https://passport.liepin.com/c/login.json?__mn__=user_login",
                       data=dict(layer_from='wwwindex_rightbox_new',
                                 user_login=username,
                                 user_pwd=passwd,
                                 chk_remember_pwd="on"), verify="GeoTrustGlobalCA.crt",
                       headers=headers)
print content.text
