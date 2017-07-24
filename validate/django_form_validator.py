#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/7/24
from django import forms


class CustomForm(forms.Form):
    name = forms.CharField(label="name", max_length=5)


if __name__ == '__main__':
    f = CustomForm({"name": "123333"})
    print f.is_valid()
