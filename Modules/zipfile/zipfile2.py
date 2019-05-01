#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-04-27 14:19
# @Author  : Xuelei Pan
# @FileName: zipfile2.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：
# @Related Links:

import zipfile

def main():
    with zipfile.ZipFile('zips.zip') as file:
        archive = file.infolist()
        lastF_info_in_zips = archive[-1]

        # print('Name of the file: - {}'.format(lastF_info_in_zips.filename))

        # print('Size of the file: - {}'.format(lastF_info_in_zips.file_size))

        # print('Is directory: - {}'.format(lastF_info_in_zips.is_dir()))

        print('File created date & time: - {}'.format(lastF_info_in_zips.date_time))



if __name__ == '__main__':
    main()