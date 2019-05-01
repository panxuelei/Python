#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-04-27 14:40
# @Author  : Xuelei Pan
# @FileName: zipfile4.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：
# @Related Links:

import zipfile

def main():
    file = 'pswd_file.zip'
    pswd = 'datacamp'

    with zipfile.ZipFile(file) as f:
        # password you pass must be in bytes.
        f.extractall(pwd=bytes(pswd, 'utf-8'))


if __name__ == '__main__':
    main()