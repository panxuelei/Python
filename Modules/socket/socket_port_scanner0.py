#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-04-23 11:02
# @Author  : Pan Xuelei
# @FileName: socket_port_scanner0.py.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：Port Scanner using Socket

from socket import *
import time

startTime = time.time()

if __name__ == '__main__':
    target = input("Enter the host to be scanned: ")
    t_IP = gethostbyname(target)
    print("Starting scan on host: ", t_IP)

    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        if(conn == 0):
            print("Port %d: OPEN" % (i,))
        s.close()

print("Time taken:", time.time() - startTime)
