#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-1-16 13:20
# @Author  : Pan Xuelei
# @FileName: yield.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：https://www.youtube.com/watch?v=bD05uGo_sVI

def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

def square_num_yield(nums):
    for i in nums:
        yield i*i

if __name__ == '__main__':
    nums = [1,2,3,4,5]
    #1
    print('square_numbers():' )
    my_nums = square_numbers(nums)
    print(my_nums, '\n')

    #2
    print('list comprehension:')
    my_nums = [x*x for x in nums]
    print(my_nums, '\n')

    #3 yield
    print('yield:')
    my_nums = square_num_yield(nums)
    print(my_nums)
    print(next(my_nums), end=' ')
    print(next(my_nums), end=' ')
    print(next(my_nums), end=' ')
    print(next(my_nums), end=' ')
    print(next(my_nums))
    # StopIteration error
    # print(next(my_nums), end=' ')

    #4 yield iteration
    print('\nyield iteration:')
    my_nums = square_num_yield(nums)
    for num in my_nums:
        print(num, end=' ')
    print('\n')

    #5 list comprehension -> yield generator
    print('list comprehension -> yield generator:')
    print('change "[" to "(":')
    # my_nums = [x * x for x in nums]
    my_nums = (x*x for x in nums)
    print(my_nums)
    print(list(my_nums))