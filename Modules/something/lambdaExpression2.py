#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-1-8 16:53
# @Author  : Pan Xuelei
# @FileName: lambdaExpression2.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：

def build_quadratic_function(a, b, c):
    '''Return the function f(x) = ax^2 + bx + c'''
    return lambda x: a*x**2 + b*x + c

f = build_quadratic_function(2, 3, -5)
print(f(0))
print(f(1))
print(f(2))

# 3*2**2 + 0*2 + 1 = 13
print(build_quadratic_function(3, 0, 1)(2))