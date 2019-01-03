#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018-12-25 20:23
# @Author  : Pan Xuelei
# @FileName: test.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：

from PIL import Image
import matplotlib.pyplot as plt

if __name__ == '__main__':
    stamp_path = 'E:\\NewFolder\\code\\Python\stamp\\测试\\test.PNG'
    pattern_path = 'E:\\NewFolder\\code\\Python\stamp\\测试\\花纹1.jpg'

    img = Image.open(pattern_path)
    gray = img.convert('L')
    plt.figure("beauty")
    plt.imshow(gray, cmap='gray')
    plt.axis('off')
    plt.show()

