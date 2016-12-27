#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/6/22
import requests
from pyquery import PyQuery as pq
import json
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig()


class Spider_Zhihu_Spider(object):

    def __init__(self, url):
        self._url = url
        self._session = requests.Session()
        self._headers = self._get_headers()
        self.get_content()

    def _get_headers(self):
        head_connection = ['Keep-Alive', 'close']
        head_accept = ['text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8']
        head_accept_language = ['zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                                'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3']
        head_user_agent = [
            'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
            ]
        cookies=('')
        header = {
            'Connection': head_connection[0],
            'Accept': head_accept[0],
            'Accept-Language': head_accept_language[0],
            'User-Agent': head_user_agent[0],
            'Cookie': cookies,
            'Accept-Encoding': 'gzip, deflate, br'
        }

        return header

    def _get_qustion_numb(self):
        o = urlparse(self._url)
        _path = o.path
        self._question_numb = _path.split('/')[-1]
        logger.debug(self._question_numb)
        return self._question_numb

    def get_content(self):

        self._content = self._session.get(url=self._url,
                                          headers=self._headers)
        # logger.debug(self._content.text)
        return self._content

    def get_title(self):
        _hqtitle = pq(self._content.text)
        self._qtitle=_hqtitle('h2.zm-item-title>span').text()
        return self._qtitle

    def get_answer_list(self):
        answer = pq(self._content.text)
        for item in answer('div.zm-item-answer'):
            iteminfo = pq(item)
            votes = iteminfo('div.answer-head>div.zm-item-vote-info>span.voters.text>a>span').text()
            answerer = iteminfo('div.zm-item-answer.zm-item-expanded>div.answer-head>div.zm-item-answer-author-info>a.author-link')
            answerername = answerer.text()
            answererlink = answerer.attr('href')
            answer_content = iteminfo('div.zm-item-rich-text>div.zm-editable-content').text()
            yield (answerername, answererlink, votes, answer_content)

        morequest = self.more_data('https://www.zhihu.com/node/QuestionAnswerListV2')

        for item in morequest['msg']:
            iteminfo = pq(item)
            votes = iteminfo(
                'div.answer-head>div.zm-item-vote-info>span.voters.text>a>span').text()
            answerer = iteminfo(
                'div.zm-item-answer.zm-item-expanded>div.answer-head>div.zm-item-answer-author-info>a.author-link')
            answerername = answerer.text()
            answererlink = answerer.attr('href')
            answer_content = iteminfo(
                'div.zm-item-rich-text>div.zm-editable-content').text()
            yield (answerername, answererlink, votes, answer_content)


    def get_data(self):
        data = {'method': 'next',
                'params': json.dumps({"url_token": int(self._get_qustion_numb()),
                           "pagesize": 10,
                           "offset": 20}),
                '_xsrf': ''}
        return data


    def more_data(self,url):
        content = self._session.post(url=url,
                                     data=self.get_data(),
                                     headers=self._headers)
        logger.debug(content.text)
        return content.json()

    def number_content(self):

        pass


if __name__ == '__main__':
    zhihu = Spider_Zhihu_Spider('https://www.zhihu.com/question/48014434')
    content = zhihu.get_answer_list()
    for item in content:
        (answerername, answererlink, votes, answer_content) = item
        print (u"({answerername}, {answererlink}, {votes}, {answer_content})".format(answerername=answerername,
         answererlink=answererlink, 
         votes=votes, 
         answer_content=answer_content))
            
