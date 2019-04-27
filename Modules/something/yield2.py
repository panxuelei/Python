#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-1-16 14:17
# @Author  : Pan Xuelei
# @FileName: yield2.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：https://www.youtube.com/watch?v=bD05uGo_sVI
# difference between list and yield generator

import memory_profiler
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve',
         'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci',
          'Arts', 'Business']


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)

    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

if __name__ == '__main__':
    mem1 = memory_profiler.memory_usage()[0]
    print('Memory (Before): {}Mb'.format(mem1))

    # list
    # t1 = time.process_time()
    # people = people_list(1000000)
    # t2 = time.process_time()


    # # yield generator
    t1 = time.perf_counter()
    people = people_generator(1000000)
    t2 = time.perf_counter()

    mem2 = memory_profiler.memory_usage()[0]
    print('Memory (After): {}Mb'.format(mem2))
    print('Memory Difference: {}Mb'.format(mem2-mem1))
    print('Took {} Seconds'.format(t2-t1))

