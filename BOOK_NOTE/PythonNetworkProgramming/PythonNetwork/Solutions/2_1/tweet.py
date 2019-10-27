# tweet.py

import urllib

def tweets(subject,nresults):
    fields = {
        'q' : subject,
        'rpp' : nresults
        }
    parms = urllib.urlencode(fields)
    u = urllib.urlopen("http://search.twitter.com/search.json?"+parms)
    data = u.read()
    return data
