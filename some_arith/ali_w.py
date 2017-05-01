#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter


def str_count(path):
    str_source = []
    with open(path, "r") as f:
        for char in f.readlines():
            str_source.append(char.strip().replace(" \n",""))

    str_source = "".join(str_source)

    c = Counter(str_source)

    dic_char_count=dict()
    for value, count in c.items():
        if not dic_char_count.get(count):
            dic_char_count[count] = []
        dic_char_count[count].append(value)
    
    for char in str_source:
        if char in dic_char_count[1]:
            return char


def i18n(in_path, out_path):
    with open(in_path, "r") as in_f:
        with open(out_path, "a") as out_f:

            lst_words = in_f.readlines()
            int_max = int(lst_words.pop(0))
            for word in lst_words:
                word = word.strip()
                if len(word) > int_max:
                    out_f.write("{start}{len}{stop}\n".format(start=word[0],len=len(word)-2,stop=word[-1]))
                else:
                    out_f.write("{word}\n".format(word=word))

                    
if __name__ == "__main__":
    print str_count("a.txt")
    i18n("words.txt","i18n_words.txt")