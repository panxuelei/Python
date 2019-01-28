#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-1-28 19:57
# @Author  : Pan Xuelei
# @FileName: youtube-dl_rename.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：给youtube-dl下载的视频重命名

# 先搁浅
import os

path = 'E:\youtube-dl'
i = 1
for video in os.listdir(path):
    newName = video.split('-')[-2]
    newName = path+ '\\' + str(i) +  newName+'.mp4'
    # os.rename
    print(newName)
    i += 1