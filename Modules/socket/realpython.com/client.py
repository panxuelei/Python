from socket import *

HOST = '127.0.0.1'
PORT = 2020

with socket(AF_INET, SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	s.sendall(b'Hello, World')
	data = s.recv(1024)
	
print('Received,', repr(data))
