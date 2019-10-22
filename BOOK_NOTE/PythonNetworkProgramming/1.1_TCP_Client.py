from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(("www.python.org", 80))   # connect
message = "GET /index.html HTTP/1.1\n\n"
message = message.encode()
s.send(message)  # send request
data = s.recv(10000).decode()  # get response
print(data)
s.close()
