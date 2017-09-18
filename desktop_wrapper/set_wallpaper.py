#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/9/18
import ctypes

SPI_SETDESKWALLPAPER = 20


def set_wallpaper(path):
    ctypes.windll.user32.SystemParametersInfoA(20, 0, path, 0x03)

if __name__ == '__main__':
    # C:\Users\Administrator\AppData\Local\Temp\wallpaper.bmp
    set_wallpaper("C:\Users\Public\Pictures\Sample Pictures\AlgaeRocks_ZH-CN13979237458_1920x1080.bmp")