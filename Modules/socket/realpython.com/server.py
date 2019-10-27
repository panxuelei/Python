from socket import *

HOST = '127.0.0.1'
PORT = 2020

with socket(AF_INET, SOCK_STREAM) as s:
	s.bind((HOST,PORT))
	s.listen()
	conn, addr = s.accept() # conn is client socket
	with conn:
		print('Connected by ', addr)
		while True:
			data = conn.recv(1024)
			if not data:
				break
			conn.sendall(data)
