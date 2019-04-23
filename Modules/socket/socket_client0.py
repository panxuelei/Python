#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-04-23 10:27
# @Author  : Pan Xuelei
# @FileName: socket_client0.py.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：Socket Client-side program

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname("PXL")
print("Remote: " + host)
port = 12345

s.connect((host, port))
msg = s.recv(1024)
msg1 = "Hello! -- FROM %s" % socket.gethostname()
s.send(msg1.encode("utf-8"))

s.close()

print(msg.decode("utf-8"))






