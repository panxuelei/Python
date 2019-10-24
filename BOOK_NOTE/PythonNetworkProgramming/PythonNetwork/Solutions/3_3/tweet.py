# tweet.py

import urllib
import json

def tweets(subject,nresults):
    fields = {
        'q' : subject,
        'rpp' : nresults
        }
    parms = urllib.urlencode(fields)
    u = urllib.urlopen("http://search.twitter.com/search.json?"+parms)
    results = json.load(u)
    return results['results']

def update(username,password,status):
    auth = urllib2.HTTPBasicAuthHandler()
    auth.add_password("Twitter API","http://twitter.com",username,password)
    opener = urllib2.build_opener(auth)

    fields = {
        'status' : status
        }
    parms = urllib.urlencode(fields)
    request = urllib2.Request("http://twitter.com/statuses/update.json",parms)
    u = opener.open(request)
    resp = u.read()
    return resp
