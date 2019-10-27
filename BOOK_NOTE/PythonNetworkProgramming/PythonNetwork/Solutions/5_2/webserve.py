# webserve.py
# Note: The program must be placed in the PythonClass/ folder

from BaseHTTPServer import HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler
from SocketServer import ThreadingMixIn

class ThreadedHTTPServer(ThreadingMixIn,HTTPServer):
    pass

import os
os.chdir("NetExercises")
serv = ThreadedHTTPServer(("",8080),CGIHTTPRequestHandler)
serv.serve_forever()
