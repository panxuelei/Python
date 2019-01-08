#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-1-3 14:40
# @Author  : Pan Xuelei
# @FileName: lambdaExpression.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：Lambda Expressions & Anonymous Functions

# Write a function to compute 3x+1
#1
def f(x):
    return 3*x + 1

print(f(2))

#2
g = lambda x: 3*x + 1
print(g(2))

# Combine first name and last name into a single "Full Name"
full_name = lambda fn, ln: fn.strip().title() + ' ' + ln.strip().title()
print(full_name(' XuELei  ', 'Pan '))

'''
lambda: 'What is my purpose?'
lambda x: 3*x + 1
lambda x, y: (x*y)**0.5
lambda x, y, z: 3/(1/x + 1/y + 1/z)
...
lambda x1, x2, ..., xn: <expression>
'''

# use last name as the sorting value
scifi_authors = ['Isaac asimov', 'Ray Brabury', 'Robert Heinlein',
                 'Arthus C. Clarke', 'Frank Herbert',
                 'Orson Scott Card', 'Douglas Adams', 'H. G. Wells',
                 'Leigh brackett']
scifi_authors.sort(key=lambda name: name.split(' ')[-1].lower())
print(scifi_authors)