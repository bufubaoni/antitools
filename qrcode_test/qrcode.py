# -*- coding: utf-8 -*-

import cv2
from pyzbar.pyzbar import decode

filepath = '2.jpeg'
image = cv2.imread(filepath)
result = decode(image)
for item in result:
    print item.type, item.data
