import urllib
from xml.etree.cElementTree import parse

def bus_prediction(route,stop):
    fields = { 'route' : route, 
               'stop' : stop }
    parms = urllib.urlencode(fields)
    u = urllib.urlopen("http://ctabustracker.com/bustime/map/getStopPredictions.jsp?"+parms)

    # Parse the XML
    predictions = []
    doc = parse(u)
    for pre in doc.findall("pre"):
        pt = pre.findtext("pt")
        predictions.append(pt)

    # Return the prediction list
    return predictions
