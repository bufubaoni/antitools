#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/6/21
import requests
from pyquery import PyQuery as pq


class Proxy_List(object):

    def __init__(self, url):
        self._url = url

    def get_headers(self):
        head_connection = ['Keep-Alive', 'close']
        head_accept = ['text/html, application/xhtml+xml, */*']
        head_accept_language = ['zh-CN,fr-FR;q=0.5',
                                'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3']
        head_user_agent = [
            'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
            'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
            'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
            'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0', ]
        self._headers = {
            'Connection': head_connection[0],
            'Accept': head_accept[0],
            'Accept-Language': head_accept_language[1],
            'User-Agent': head_user_agent[3]
        }

    def get_content(self):
        session = requests.Session()
        self._content = session.get(url=self._url,
                                    headers=self._headers)
        self._session = session
        return self._content

    def get_cssurl(self):
        csscontent = pq(self._content.text)
        css = csscontent('link')
        link = pq(css[1])
        self._cssurl = link.attr('href')
        return self._cssurl

    def get_class(self):
        linelist = self._csscontent.text.split('\n')
        self._csslist = dict()
        for line in linelist:
            item = line.split(' ')
            if item[0]:
                dc = item[1].split('"')
                self._csslist[item[0][1:6]] = dc[1]
        return self._csslist

    def get_class_source(self):
        session = requests.Session()
        self._csscontent = session.get(url=(self._url[:-7] + self.get_cssurl()),
                                             headers=self.get_headers())
        return self._csscontent

    def get_proxy_list(self):
        self.get_headers()
        self.get_content()
        self.get_cssurl()
        self.get_class_source()
        self.get_class()
        hp = pq(self._content.text)
        csslist = self._csslist
        for item in hp('table#proxylist>tr'):
            raw = pq(item)
            if raw('td>span').attr('class'):
                yield (
                raw('td').text().split()[0], csslist[raw('td>span').attr('class')],
                raw('td').text().split()[4])


if __name__ == '__main__':
    '''初始化一下即可针对 此网站进行抓代理'''
    listip = Proxy_List('http://www.samair.ru/proxy/')
    for item in listip.get_proxy_list():
        print(item)
