#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging

from django import forms
from django.views.generic import View
from django.shortcuts import HttpResponse

logger = logging.getLogger(__name__)
from django.views.decorators.csrf import csrf_exempt


class ApiView(View):
    ALLOWED_METHOD = None

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.response_data = {"msg": "ok",
                              "status": "-1",
                              "data": {}}

        if request.method in [item.upper() for item in self.ALLOWED_METHOD]:
            method = getattr(self, request.method.lower())
            if request.method.lower() in ["post",]:
                self.request.data = json.loads(u"".join([item.decode("utf8")for item in self.request.readlines()]))
            respose = method(request, *args, **kwargs)
            if isinstance(respose, (list, dict)):
                self.response_data["data"] = respose
                self.response_data["status"] = "1"
            else:
                self.response_data["msg"] = respose
            return HttpResponse(json.dumps(self.response_data, ensure_ascii=False), status=200,
                                content_type=" application/json")


class ValidatorsMixin(object):
    SCHEMA = None

    def get_schema(self):

        class _CustomForm(forms.Form):
            pass

        if self.SCHEMA:
            for key, value in self.SCHEMA.items():
                _value = dict()
                _value.update(**value)
                _field_type = _value.pop("type")
                _CustomForm.declared_fields.update({key: getattr(forms, self.__reflection[_field_type])(**_value)})

        return _CustomForm

    def validator(self, param):
        return self.get_schema()(param)

    def cleaned(self):
        self.form = self.validator(self.request.data)
        if not self.form.is_valid():
            return False
        else:
            return True

    __reflection = {
        "int": "IntegerField",
        "string": "CharField",
        "datetime": "DateTimeField",
        "date": "DateField",
        "decimal": "DecimalField",
        "regex": "RegexField",
        "float": "DecimalField"
    }
