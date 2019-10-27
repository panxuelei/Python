# pickle_xmlrpc.py
from SimpleXMLRPCServer import SimpleXMLRPCServer
import pickle

def command(encobj):
    obj = pickle.loads(encobj)
    print repr(obj)
    # Note: the repr() function prints out the representation of
    # an object using Python syntax.
    return True

serv = SimpleXMLRPCServer(("",45000))
serv.register_function(command)
serv.serve_forever()
