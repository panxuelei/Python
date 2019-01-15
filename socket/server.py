#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-1-14 15:59
# @Author  : Pan Xuelei
# @FileName: server.py.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：

import socket

HOST = '127.0.0.1' # Standard loopback interface address(localhost)
PORT = 65432 # Port to listen on(non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by ', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('From:' + addr[0])
            conn.send(b'Hi, here is Server!')



