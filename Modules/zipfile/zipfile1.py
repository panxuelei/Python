#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-04-27 13:59
# @Author  : Xuelei Pan
# @FileName: zipfile1.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：
# @Related Links:

import zipfile

def main():
    with zipfile.ZipFile('zips.zip') as file:
        # # ZipFile.infolist() returns  a list containing all
        # # the members of an archive file
        # print(file.infolist())

        # # ZipFile.namelist() returns a list containing all
        # # the members with names of an archive file
        # print(file.namelist())

        # # ZipFile.getinfo(path=filepath) returns the information
        # # about a member of Zip file.
        # print(file.getinfo(file.namelist()[-1]))

        # # ZipFile.open(name=filename, mode=mode_type, pwd = password)
        # # opens the members of an archive file.
        # # 'pwd' is optional
        # text_file = file.open(name=file.namelist()[2], mode='r')
        # print(text_file.read())
        # text_file.close()

        # ZipFile.extractall(folder, pwd=password)
        # extracts all the files to 'folder'(def = current directory)
        file.extractall('temp')


if __name__ == '__main__':
    main()