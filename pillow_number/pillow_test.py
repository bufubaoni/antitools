#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by alex on 2017/3/21
from random import Random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

number = "4556"


# im = Image.new('RGBA', (100, 40), (255,) * 4)
#
# r = Random()
# draw = ImageDraw.ImageDraw(im)
#
# draw.text((0, 0), number, fill=(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)))
#
# im.save("test.jpg")


def code_img(code, size):
    r = Random()
    code = code
    len_code = len(code)

    font = ImageFont.truetype("Essence_Sans.ttf", size)

    font_width, font_height = font.getsize(code)
    font_width += size / 2
    print font_width, font_height
    img = Image.new("RGBA", (font_width, font_height), (255,) * 4)

    draw = ImageDraw.ImageDraw(img)

    draw.text((size/10, -size/10), code, font=font, fill=(0, 0, 0))

    params = [1,
              0,
              0,
              0,
              1 - float(r.randint(1, 10)) / 100,
              0,
              0.001,
              float(r.randint(1, 2)) / 500
              ]
    print params
    img = img.transform((font_width, font_height), Image.PERSPECTIVE, params)
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

    img.save("test.jpg")


if __name__ == "__main__":
    code_img(number, 35)
