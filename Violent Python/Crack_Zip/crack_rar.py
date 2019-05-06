#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-06 16:48
# @Author  : Xuelei Pan
# @FileName: crack_rar.py.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：
# @Related Links:

# https://blog.csdn.net/Big_talent/article/details/52367184
# https://blog.csdn.net/q1w2e3r4470/article/details/51859467
# 记得重启系统

from unrar import  rarfile

dictionary = 'E:\\NewFolder\\code\\Python\\Violent Python\\Crack_zip\\dictionary.txt'
file = ''
extract_to = '\\'.join(file.split('\\')[0:-1])+ '\\' + file.split('\\')[-1].split('.')[0]
print(extract_to)
print("Hi")
rar = rarfile.RarFile(file)
print("Start")

with open(dictionary, 'r') as p:
    p = p.readlines()
    for password in p:
        password = password.strip('\n')
        print(password)
        if(rar.extractall(path=extract_to,pwd=password)):
            break
        else:
            continue

