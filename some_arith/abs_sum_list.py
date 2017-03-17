#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import combinations
import copy

def abs_sum(listA,listB):
    len_listA = len(listA)
    len_listB = len(listB)

    list_all = []
    
    list_all.extend(listA)
    list_all.extend(listB)

    len_min = len_listB  if len_listA > len_listB else len_listA
    
    min_list = combinations(list_all, len_min)

    col_A_B = []
    min_abs = None

    for list_test in min_list:
        max_list = copy.deepcopy(list_all)
        for item in list_test:
            max_list.pop(max_list.index(item))
        col_A_B.append((list_test,max_list))
        tem  = abs(sum(list_test)-sum(max_list)), list_test, max_list
        if min_abs:
            if tem[0] < min_abs[0]:
                min_abs = tem
        else :
            min_abs = tem

        if min_abs[0]==0:
            return min_abs
 
    return min_abs


if __name__ == "__main__":
    print abs_sum([62, 181, 106, 814, 892, 504, 890, 100, 24, 640],[ 684, 939, 749, 970, 596, 605, 194, 193, 127, 173])
