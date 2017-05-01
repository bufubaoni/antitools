#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/4/1
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' * self.__class__.__name__, self.name

    def __get__(self, instance, owner):
        print "ok"
        return 666


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, "str")


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return type.__new__(cls, name, bases, attrs)

        mapping = dict()

        for k, v in attrs.items():
            if isinstance(v, Field):
                mapping[k] = v
        for k in mapping.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mapping
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


class Test():
    pass

