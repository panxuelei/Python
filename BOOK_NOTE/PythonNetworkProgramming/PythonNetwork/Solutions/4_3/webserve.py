# webserve.py
# Note: The program must be placed in the PythonClass/ folder

from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import os
os.chdir("NetExercises")
serv = HTTPServer(("",8080),SimpleHTTPRequestHandler)
serv.serve_forever()
