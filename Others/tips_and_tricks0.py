# https://www.geeksforgeeks.org/10-essential-python-tips-tricks-programmers/
# # In-Place Swapping of two numbers.
# x, y = 10, 20
# print(x, y)
# x, y = y, x
# print(x, y)

# # Reversing a string
# a = "12345"
# print('\'12345\' Reverse is', a[::-1])

# # Greate s single string from all the elements in list
# a = ['Geeks', 'For', 'Geeks']
# print('-'.join(a))

# # Chaining of comparison operators
# n = 10
# result = 1 < n < 20
# print(result)
# result = 1 > n <= 9
# print(result)

# # print the file path of imported modules
# import os
# import socket
# print(os)
# print(socket)

# # use of enums in python
# class MyName:
#     a, For, Geeks = range(3)
#
# print(MyName.a)
# print(MyName.For)
# print(MyName.Geeks)

# # return multiple values from functions
# def X():
#     return 1,2,3,4
#
# a,b,c,d = X()
#
# print(a,b,c,d)

# # check the memory usage of an object
# import sys
# x = 'ab'
# print(sys.getsizeof(x))

# # print string n times
# n = 2;
# a = 'Geeks'
# print(a*n)

# checking if two words are anagrams
from collections import Counter
def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)

print(is_anagram('geek', 'eegk'))
print(is_anagram('geek', 'peek'))

