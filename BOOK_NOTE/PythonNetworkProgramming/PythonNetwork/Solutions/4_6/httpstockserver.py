# httpstockserver.py

# A stand-alone HTTP server that feeds real-time stock quotes.
# Stock quote data is obtained from Yahoo, but in reality you
# would use some other internal data source (data source, 
# real-time feed, etc.)

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from string import Template
import urllib, csv

# Output template that we'll fill in with various fields
output = Template("""<?xml version="1.0"?>
<quote>
   <stock>
       <symbol>$symbol</symbol>
       <name><![CDATA[$name]]></name>
       <price>$price</price>
       <change>$change</change>
       <percent>$percent</percent>
       <date>$date</date>
       <time>$time</time>
       <open>$open</open>
       <high>$high</high>
       <low>$low</low>
       <volume>$volume</volume>
    <stock>
<quote>
""")

class StockHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path[1:]

        # Fetch data about the selected stock
        request = {
            's' : s,
            'f' : 'snl1d1t1c1p2ohgv',
            'e' : '.csv'
            }

        parms = urllib.urlencode(request)

        u = urllib.urlopen("http://download.finance.yahoo.com/d/quotes.csv?"+parms)
        reader = csv.DictReader(u,['symbol','name','price','date','time','change','percent',
                               'open','high','low','volume'])

        record = reader.next()
        self.send_response(200,"OK")
        self.send_header('Content-type','application/xml')
        self.end_headers()
        self.wfile.write(output.substitute(record))

serv = HTTPServer(("",44000),StockHandler)
serv.serve_forever()
