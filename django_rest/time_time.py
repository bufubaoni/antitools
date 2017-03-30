#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/3/29
from time import time
from requests import Session

session = Session()


class APIView(object):
    pass


def method_decorator(a):
    pass


def modify_token_exists():
    pass


class InfoWirelessGateway(object):
    object = "1"


class RelationCompanyDtu(object):
    object = "1"


class InfoCompany(object):
    object = "1"


def response(*a):
    pass


class GatewayNote(APIView):
    """
        对指定的网关设备进行备注
    """

    @method_decorator(modify_token_exists)
    def post(self, request, user_id=None):

        dtu_id, company_name = [request.data.get(k) for k in ["id", "company_name"]]

        try:
            check_info_wireless = InfoWirelessGateway.objects.filter(sn=dtu_id).update(alias=company_name + str(dtu_id))
            assert check_info_wireless
            check_relation = RelationCompanyDtu.objects.filter(dtu_id=dtu_id)
            assert check_relation
            check_info = InfoCompany.objects.filter(id=check_relation[0].company_id) \
                .update(company_name=company_name + str(check_relation[0].company_id))
            assert check_info
        except AssertionError:
            return response({}, u"抱歉此设备不存在", False)

        return response({}, u"ok", True)

# def test():
#     try:
#         assert False
#         print "no error"
#     except AssertionError:
#         print "error"


if __name__ == "__main__":
    # test()
    pass