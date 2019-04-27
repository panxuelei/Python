#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-04-27 14:30
# @Author  : Xuelei Pan
# @FileName: zipfilee3.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：
# @Related Links:

import zipfile

def main():
    file = 'zips.zip'

    with zipfile.ZipFile(file, 'r') as f:
        # print all the information of archive file contents
        # use 'printdir()' method.
        # name, time, size
        print(f.printdir(), '\n')

        print('Extracting all files...')
        f.extractall()
        print('Done!')

if __name__ == '__main__':
    main()