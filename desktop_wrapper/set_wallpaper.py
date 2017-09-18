#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ChenXin on 2017/9/18
import ctypes


def set_wallpaper(path):
    SPI_SETDESKWALLPAPER = 20
    return ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, str(path), 0x03)


if __name__ == '__main__':
    # C:\Users\Administrator\AppData\Local\Temp\wallpaper.bmp
    print set_wallpaper("C:/WhipCoral_ZH-CN10285480118_1920x1080.jpg")
