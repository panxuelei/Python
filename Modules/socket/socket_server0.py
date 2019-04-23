#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-04-23 10:15
# @Author  : Pan Xuelei
# @FileName: socket_server0.py.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：Socket Server-side program

import socket

def Main():
    host = socket.gethostbyname("PXL")
    print(host)
    print(socket.gethostname())
    port = 12345

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(0)

    print("Socket is listening......")

    while True:
        # accept() return a tuple
        # conn is a socket element, same as line 17.
        client_socket, client_IP_port = server_socket.accept()
        print("Got connection from %s" % str(client_IP_port))
        msg = "Connecting Established. -- FROM %s\n" % socket.gethostname()
        client_socket.send(msg.encode("utf-8"))
        print(client_socket.recv(1024).decode("utf-8"))

if __name__ == '__main__':
    Main()