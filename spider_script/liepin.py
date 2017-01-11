#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/11
from requests import Session
import requests

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
           'Cookie': '__tlog=1484103846822.92%7C00000000%7C00000000%7C00000000%7C00000000; abtest=0; verifycode=e163c1bdb3f641a78c7d491e0b5790e1; _fecdn_=1; __uuid=1484103849760.22; __session_seq=1; __uv_seq=1; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1483428418,1484102217; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1484103856; _mscid=00000000; _uuid=8B7BB17AFFA8440B23F0FB0CC04CA6BF; 1f0241fc=ea21a4c007f803dccdbb8595d630d088',
           'Connection': 'keep-alive'
           }


content = session.post("https://passport.liepin.com/c/login.json?__mn__=user_login",
                       data=dict(layer_from='wwwindex_rightbox_new',
                                 user_login=username,
                                 user_pwd=passwd,
                                 chk_remember_pwd="on"), verify="GeoTrustGlobalCA.crt",
                       headers=headers)
print content.text
