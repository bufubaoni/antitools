#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Alex on 2017/1/25
from Crypto.Cipher import DES
import base64


def decrydes(content):
    key = content[:8]
    _content = content[8:]
    _obj = DES.new(key, DES.MODE_ECB)
    return _obj.decrypt(base64.decodestring(_content)).strip("\x08")

import json


if __name__ == "__main__":
    # st = "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"
    # print decrydes(st)
    print '1k A={"z":4,"B":"3","D":"4.0","C":y,"u":t,"v":"x","w":["L-K.0.2","M-O.0.2","N-J.0.2","F-E.0.2","G-I.0.2","H-s.0.2","c-b.0.2","a-f.0.2","e-d.0.2","6-5.0.2","7-8.0.2","9-o.0.2","p-r.0.2","q-m.0.2","i-h.0.2","j-l.0.2","k-n.0.2","P-14.0.2","1j-1l.0.2","1n-1m.0.2","1i-1e.0.2","1d-1f.0.2","1h-1g.0.2","1w-1v.0.2","1u-1y.0.2","1x-1t.0.2","1p-1o.0.2","1q-1s.0.2","1r-1c.0.2","X-W.0.2","Y-10.0.2","Z-V.0.2","R-Q.0.2","S-U.0.2","T-18.0.2"],"17":19,"1b":1a,"16":"/12/g/3[11]/13/","15":1}||{};', 62, 97, 'jpg||webp|古惑仔|8928|17670|iieye0010|iieye0011|35049|iieye0012|iieye0008|34356|iieye0007|11203|iieye0009|16948||15028|iieye0015|iieye0016|iieye0017|18098|16560|49408|62953|iieye0013|iieye0014|16663|46772|87948|cid|cname|files|第002卷|null|bid|cInfo|bname|burl|bpic|17601|iieye0004|iieye0005|iieye0006|41546|11127|10960|iieye0001|iieye0002|iieye0003|92312|iieye0018|13888|iieye0033|iieye0034|iieye0035|17439|26660|60093|iieye0030|iieye0031|iieye0032|65963|牛佬|ps4|Vol_002|19244|status|path|finished|13878|false|35|len|74951|iieye0022|91373|35842|15288|iieye0023|iieye0021|iieye0019|var|29493|21181|iieye0020|11701|iieye0027|iieye0028|iieye0029|26875|12251|iieye0025|39592|iieye0024|iieye0026|21208'.split('|')

