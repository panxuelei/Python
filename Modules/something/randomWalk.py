#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018-12-29 17:08
# @Author  : Pan Xuelei
# @FileName: randomWalk.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：Random Walk

import random

def random_walk(n):
    '''Return coordinates after "n" block random walk.'''
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x + 1
        else:
            x = x - 1
    return (x, y)


for i in range(25):
    walk = random_walk(10)
    print(walk, 'Distance from home = ',
          abs(walk[0]) + abs(walk[1]))