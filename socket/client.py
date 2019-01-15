#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-1-14 16:04
# @Author  : Pan Xuelei
# @FileName: client.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：

import socket

HOST = '127.0.0.1' # The server's hostname or IP address
PORT = 65432 # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(b'Hello, here is client!')
    data = s.recv(1024)

print('Received', repr(data))