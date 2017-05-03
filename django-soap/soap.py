#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/5/3
from django.views.generic import View
from pysimplesoap.server import SoapDispatcher
from django.http import HttpResponse
from abc import abstractmethod


class SoapView(View):
    SOAP = SoapDispatcher(name="test",
                          action="http://127.0.0.1:8000/soap/",
                          location="http://127.0.0.1:8000/soap/",
                          namespace="namespace",
                          soap_ns="xs",
                          prefix="pys")
    NAME = None
    RESAULT = None
    NS = None
    ARG = None
    URL_KW = {}

    def dispatch(self, *args, **kwargs):
        # pdb.set_trace()
        request = args[0]
        location = request.META.get("HTTP_SOAPACTION", None)
        if self.NAME:
            self.SOAP.name = self.NAME
        if self.NS:
            self.SOAP.soap_ns = self.NS
        for k, v in kwargs.items():
            self.URL_KW[k] = v
        if location:
            self.SOAP.action = location
            self.SOAP.location = location

        self.SOAP.register_function("test", self.soap, self.RESAULT, args=self.ARG)
        return super(SoapView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponse(self.SOAP.wsdl(), content_type="text/xml")

    def post(self, request, *a, **kw):
        xml = self.SOAP.dispatch(request.body, fault={})
        return HttpResponse(xml, content_type="text/xml")

    @abstractmethod
    def soap(self, *a, **kw):
        pass
