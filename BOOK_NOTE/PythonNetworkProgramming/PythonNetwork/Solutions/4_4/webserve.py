# webserve.py
# Note: The program must be placed in the PythonClass/ folder

from BaseHTTPServer import HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler
import os
os.chdir("NetExercises")
serv = HTTPServer(("",8080),CGIHTTPRequestHandler)
serv.serve_forever()
