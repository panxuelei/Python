import urllib

def bus_prediction(route,stop):
    fields = { 'route' : route, 
               'stop' : stop }
    parms = urllib.urlencode(fields)
    u = urllib.urlopen("http://ctabustracker.com/bustime/map/getStopPredictions.jsp?"+parms)
    return u.read()
