#!/usr/bin/env python
# -*- coding: utf-8 -*-


def list_sort(list_source=[]):
    
    dic_count = {value:list_source.count(value) for value in list_source}
    
    _resault = []

    for item in range(max(dic_count.values())):
        _resault.append(list())

    for item in list_source:
        r_index = -(list_source.count(item))
        if item not in _resault[r_index]:
            _resault[r_index].append(item)
    
    _resault = reduce(lambda x, y: x + sorted(y, reverse = True), _resault)
    return _resault
    

if __name__ == "__main__":
    print list_sort([1,1,1,1,2,2,2,2,3,4,4,5])