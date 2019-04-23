#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-04-23 11:43
# @Author  : Pan Xuelei
# @FileName: ping_sweep0.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：Port Scanner using ICMP(Live hosts in a network)
# @Related Links: https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_quick_guide.htm

import os
import platform
from datetime import datetime

net = input('Enter the Network Address: ')
net1 = net.split('.')
a = '.'

net2 = net1[0] + a + net1[1] + a + net1[2] + a
st1 = int(input('Enter the Starting Number: '))
en1 = int(input('Enter the Last Number: '))
en1 += 1
oper = platform.system()

if(oper == 'Windows'):
    ping1 = 'ping -n 1 '
elif(oper == 'Linux'):
    ping1 = 'ping -c 1'
else:
    ping1 = 'ping -c 1'

t1 = datetime.now()
print('Scanning in Progress: ')

for ip in range(st1, en1):
    addr = net2 + str(ip)
    comm = ping1 + addr
    response = os.popen(comm)

    for line in response.readlines():
        if(line.count('TTL')):
            break;
        if(line.count('TTL')):
            print(addr, '--> Live')

t2 = datetime.now()
total = t2 - t1
print('Scanning completed in: ', total)