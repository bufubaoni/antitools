# -*- coding: utf-8 -*-
import urllib
import json
import os
import time 
os.system("chcp 65001")
request = urllib.urlopen

def getword(word):
    params=urllib.urlencode({"Word":word})
    f=request("http://xtk.azurewebsites.net/BingDictService.aspx?{params}".format(params=params))
    try:
        getjson=json.loads(f.read())
        f.close()
    except:
        return None
    return getjson

def prettyprint(wordjson):
    if wordjson and wordjson["word"]:
        if wordjson["pronunciation"] and wordjson["pronunciation"]["AmE"]:
            print("{word}---/{pronunciation}/".format(word=wordjson["word"],pronunciation=wordjson["pronunciation"]["AmE"].encode("utf8")))
        for index, defd in enumerate(wordjson["defs"]):
            print("{index}-pos:{pos} def:{defd}".format(index=index,pos=defd["pos"],defd=defd["def"].encode("utf8")))
    else:
        print("no words")

    
def dictword(word):
    prettyprint(getword(word))

if __name__ == "__main__":
    while True:
        words = raw_input("input your words:")
        dictword(words)




