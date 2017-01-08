#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/8
class RunableMixin(object):
    def run(self):
        print "I can runing"


class StandMixin(object):
    def stand(self):
        print "I can stand"

class Man(RunableMixin,StandMixin):
    pass

if __name__ == "__main__":
    person = Man()
    person.run()
    person.stand()