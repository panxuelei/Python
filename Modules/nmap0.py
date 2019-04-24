#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-04-24 9:25
# @Author  : Pan Xuelei
# @FileName: nmap0.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：Developing An Nmap Scanner
# @Related Links: https://www.youtube.com/watch?v=1lh_SkY8cHk&list=PLBf0hzazHTGM_dncTqO9l-0zUQYP0nNPU&index=4

import nmap

scanner = nmap.PortScanner()
print(type(scanner))

print('Welcome, this is a simple nmap automation tool')
print('<--------------------------------------------->')

ip_addr = input('Please enter the IP address you want to scan: ')
print('The IP you entered is: ', ip_addr)

resp = input('''\nPlease enter the type of scan you want to ruan
                 1)SYN ACK Scan
                 2)UDP Scan
                 3)Comprehensive Scan\n''')

print('You have selected option: ', resp)

if resp == '1':
    print('Nmap Version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print('IP Status: ', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print('Open Ports: ', scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print('Nmap Version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1000-1024', '-v -sU')
    print(scanner.scaninfo())
    print('IP Status: ', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print('Open Ports: ', scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print('Nmap Version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '10-24', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print('IP Status: ', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print('Open Ports: ', scanner[ip_addr]['tcp'].keys())
else:
    print('Please enter a valid option.')