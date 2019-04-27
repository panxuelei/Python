#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-1-11 18:10
# @Author  : Pan Xuelei
# @FileName: sortingInPy.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：

planets = [
    ('Mercury', 2440, 5.43, 0.395),
    ('Venus', 6052, 5.24, 0.723),
    ('Earth', 6378, 5.52, 1.000),
    ('Mars', 3396, 3.93, 1.530),
    ('Jupiter', 71492, 1.33, 5.210),
    ('Saturn', 60268, 0.69, 9.551),
    ('Uranus', 25559, 1.27, 19.213),
    ('Neptune', 24764, 1.64, 30.070)
]

size = lambda planet: planet[1]
planets.sort(key=size, reverse=True)
print(planets)

# sort() method can't sort tuple,string
# sorted() method does
num = (3,2,1,4,6,8,0,5,7,9)
print(sorted(num))
print(num)