# -*- coding: utf-8 -*-
import urllib
import time
from datetime import datetime


def urlopen(url):
    try:
        return urllib.urlopen(url=url)
    except:
        return None

def server_test(url):
    print(datetime.now().isoformat())
    if urlopen(url):
        print("The server is runing !")
    else:
        print("The server is stop")

def run(url):
    while True:
        server_test(url)
        time.sleep(5)

if __name__ == "__main__":
    run("http://192.168.1.110")