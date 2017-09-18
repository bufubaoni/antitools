#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/9/18

from bing_uri import save_wrapper, uri

from set_wallpaper import set_wallpaper


def main():
    path = save_wrapper(uri)
    print path
    set_wallpaper(path)


if __name__ == '__main__':
    main()
