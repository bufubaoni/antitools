#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/23
from pyquery import PyQuery as pq
from requests import Session

sesson = Session()


def get_dijiye_from():
    urlss = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1, 6, 1)]
    return urlss


def get_links_from():
    _urls = get_dijiye_from()
    for url in _urls:
        content = sesson.get(url)
        for item in pq(content.text)("#page_list>ul>li>a"):
            yield pq(item).attr("href")


def get_items_info():
    for url in get_links_from():
        content = sesson.get(url)
        pq_h = pq(content.text)
        yield dict(title=pq_h("title")[0].text,
                   address=pq(pq_h("div.pho_info>p")[0]).attr("title") or None,
                   price=pq_h("div#pricePart>div>span")[0].text,
                   name=pq_h("a.lorder_name")[0].text, )


if __name__ == "__main__":
    for i in get_items_info():
        print i
