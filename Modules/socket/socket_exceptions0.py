#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-04-23 10:43
# @Author  : Pan Xuelei
# @FileName: socket_exceptions0.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：Handling network socket exceptions

import socket

host = "192.168.10.155"
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    s.bind((host, port))
    s.settimeout(3)
    data, addr = s.recvfrom(1024)
    print("recevied form ", addr)
    print("obtained ", data)
    s.close()
except socket.timeout:
    print("No connection between client and server.")
    s.close()
