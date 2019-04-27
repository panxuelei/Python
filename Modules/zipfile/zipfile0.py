#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-04-27 13:57
# @Author  : Xuelei Pan
# @FileName: zipfile0.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：
# @Related Links:https://www.datacamp.com/community/tutorials/zip-file


import  zipfile

def main():
    try:
        with zipfile.ZipFile('zips.zip') as file:
            print('File size is compatible')
    except zipfile.LargeZipFile:
        print('Error: File size is too large.')

if __name__ == '__main__':
    main()

    print(zipfile.is_zipfile('zips.zip'))
