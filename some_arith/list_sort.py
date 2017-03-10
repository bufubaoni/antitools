#!/usr/bin/env python
# -*- coding: utf-8 -*-


def list_sort(list_source=[]):
    
    dic_count = {value:list_source.count(value) for value in list_source}
    
    _resault = []

    for item in range(max(dic_count.values())+1):
        _resault.append(list())
    
    for item in list_source:
        r_index = -(list_source.count(item))
        if item not in _resault[r_index]:
            _resault[r_index].append(item)
    
    _resault = reduce(lambda x, y: x + sorted(y, reverse = True), _resault)
    return _resault


from collections import Counter

def list_sort_b(list_source=[]):
    dic_count = Counter(list_source)
    _r_order_list = sorted(dic_count.items(), lambda x, y: cmp(x[1], y[1]), key=lambda x: x)
    _order_list = list(reversed([item[0] for item in _r_order_list]))
    return _order_list


if __name__ == "__main__":
    print list_sort([1,1,2,2,3])
    print list_sort_b([1,1,2,2,3])