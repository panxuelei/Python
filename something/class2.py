#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018-12-29 11:36
# @Author  : Pan Xuelei
# @FileName: class2.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：
import datetime

class User:
    '''This is the docstring.'''
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday # yyyymmdd

        # Extract first and last name
        name_pieces = full_name.split(' ')
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        '''Return the age of the user in years.'''
        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd) # Date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        print(dob)
        return age_in_years

user = User('Xuelei Pan', '19960328')
# print(user.name)
# print(user.first_name)
# print(user.last_name)
# print(user.birthday)
print()
print(user.age())
# help(User)