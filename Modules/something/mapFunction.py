#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-1-8 17:03
# @Author  : Pan Xuelei
# @FileName: mapFunction.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：

import math

def area(r):
    '''Area of a circle with radius 'r'.'''
    return math.pi * (r**2)

radii = [2, 5, 7.1, 0.3, 10]

# Method 1: Direct method

areas = []
for r in radii:
    a = area(r)
    areas.append(a)

print(areas)

