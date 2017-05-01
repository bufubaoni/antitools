#!/usr/bin/env python
# -*- coding: utf-8 -*-
from marionette_driver.marionette import Marionette
import pdb

client = Marionette("localhost", port=2828)

client.start_session()

client.navigate("http://www.tianyancha.com/company/75507246")

element = client.find_element("class name", 'company_info')

print element.text

