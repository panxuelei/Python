# busloc.py
from xml.etree.cElementTree import iterparse

def bus_locations(f):
    for event, elem in iterparse(f,('start','end')):
        if event == 'start' and elem.tag == 'buses':
            buses = elem
        elif event == 'end' and elem.tag == 'bus':
            print "%s,%s,%s,%s,%s" % (
                elem.findtext('id'),
                elem.findtext('route'),
                elem.findtext('direction'),
                elem.findtext('latitude'),
                elem.findtext('longitude')
                )
            # Discard the bus element by removing it from the parent
            buses.remove(elem)

# Example use
if __name__ == '__main__':
    bus_locations(open("../../Data/allroutes.xml"))



    
