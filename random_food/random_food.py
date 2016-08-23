#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2016/7/7
import random
import time
import sys


_ver = sys.version_info

is_py2 = (_ver[0]==2)
is_py3 = (_ver[0]==3)

#添加食物即可
foodlist = [u"千里香", u"私家面", u'齐妈妈', u'kfc19元套餐', u'kfc19.5元套餐']


def get_random_number(seed, len_foodlist):
    random.seed(seed)
    random_number = random.randint(0, len_foodlist-1)
    return random_number


def get_food(foodlist, random_number):
		return foodlist[random_number]
	


def choocie_food(foodlist):
    seed = time.time()
    len_foodlist = len(foodlist)
    random_number = get_random_number(seed, len_foodlist)
    print(get_food(foodlist, random_number))

if __name__ == '__main__':
    choocie_food(foodlist)
    if is_py2:
        key = raw_input("press any key to exit!")
    else:
        key = input("press any key to exit!")
