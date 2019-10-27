#!/usr/bin/env python

# A template string containing the desired output.  Modify
# as needed to change the output

from string import Template
temp = Template("""\
<b>$symbol</b> ($name)<br>
<font size=+2><b>$price</b></font> 
<font color="$color">$change ($percent)</font> 
$date $time <br>
<table>
<tr><td>Open:</td><td>$open</td><td>Volume:</td><td>$volume</td></tr>
<tr><td>High:</td><td>$high</td><td>Low:</td><td>$low</td></tr>
</table>
""")

# Get form fields
import cgi
fields = cgi.FieldStorage()
s = fields.getvalue('s')

# Fetch data about the selected stock
request = {
    's' : s,
    'f' : 'snl1d1t1c1p2ohgv',
    'e' : '.csv'
}

import urllib, csv
parms = urllib.urlencode(request)

u = urllib.urlopen("http://download.finance.yahoo.com/d/quotes.csv?"+parms)
reader = csv.DictReader(u,['symbol','name','price','date','time','change','percent',
                           'open','high','low','volume'])

record = reader.next()

record['color'] = 'red'
try:
    if float(record['change']) > 0:
        record['color'] = 'green'
except ValueError:
    pass

# Render the template with appropriate variables filled in
print "Content-type: text/html\r"
print '\r'
print temp.substitute(record)
