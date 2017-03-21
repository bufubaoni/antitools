#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by alex on 2017/3/21
from random import Random
from PIL import Image, ImageDraw

number = "455613"
im = Image.new('RGBA', (100, 40), (255,) * 4)

r = Random()
draw = ImageDraw.ImageDraw(im)

draw.text((0, 0), number, fill=(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)))

im.save("test.jpg")
