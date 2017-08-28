#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/8/28
crypt_str = "defghigklmnopqrstuvwxyzabc"

current_str = "abcdefghigklmnopqrstuvwxyz"


def encrypt(code):
    result = ""
    for i in code:
        if i in current_str:
            p_i = current_str.index(i)
            result += crypt_str[p_i]
        else:
            result += i
    return result


def decrypt(code):
    result = ""
    for i in code:
        if i in crypt_str:
            p_i = crypt_str.index(i)
            result += current_str[p_i]
        else:
            result += i
    return result


if __name__ == '__main__':
    print encrypt("i love you !")
    print decrypt("l oryh brx !")
