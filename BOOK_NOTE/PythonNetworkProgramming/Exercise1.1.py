from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(("www.python.org", 80))
message = "GET /index.html HTTP/1.0\r\n\r\n"
s.send(message.encode())
chunks = []

while True:
	chunk = s.recv(10000).decode()
	if not chunk: break
	chunks.append(chunk)

s.close()
response = "".join(chunks)
print(response)
