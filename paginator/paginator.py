# -*- coding: utf-8 -*-
from sqlalchemy.orm.query import Query


class Page(object):
    '''
    total
    offset
    limit
    '''

    def __init__(self, items, total, offset, limit):
        self.items = items
        self.total = total
        self.offset = offset
        self.limit = limit


def paginate_query(query, offset=0, limit=0):
    is_need_paginate = offset or limit
    total = query.count()
    if not is_need_paginate:
        items = query.all()
        return Page(items, total, offset, total)
    items = query.limit(limit).offset(offset).all()
    return Page(items, total, offset, limit)


def paginate_list(list_items, offset=0, limit=0):
    items = []
    is_need_paginate = offset or limit
    total = len(list_items)

    if not is_need_paginate:
        return Page(list_items, total, 0, total)

    offset = offset
    index = offset
    if offset==0 and limit==0:
        return Page(list_items, total, offset, limit)
    while index < total and len(items) < limit:
        items.append(list_items[index])
        index = index + 1
    return Page(items, total, offset, limit)


def paginate(query, offset=0, limit=0):
    if isinstance(query, Query):
        return paginate_query(query, offset, limit)
    elif isinstance(query, (tuple, list)):
        return paginate_list(query, offset, limit)
    else:
        raise TypeError("got a %s but %s %s or %s needed" % type(query), list, tuple, Query)
