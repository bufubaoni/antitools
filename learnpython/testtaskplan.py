# -*- coding: utf-8 -*-
import datetime
import os

BASEPATH=os.path.dirname(os.path.abspath(__file__))


with open(BASEPATH+"/a.txt","a") as f:
    f.write(datetime.datetime.now().isoformat()+"\n")