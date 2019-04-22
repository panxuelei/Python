# https://www.youtube.com/watch?v=LosIGgon_KM

from urllib import request

url0 = "https://google.com"
url1 = "https://youtube.com"
url2 = "https://www.wikipedia.org/"
resp = request.urlopen(url2)

print(type(resp))
print(resp.code)
print(resp.length)
# see part of the response, not all
# print(resp.peek())
data = resp.read()
print(type(data))
print(len(data))
# change the response to string
html = data.decode("utf-8")
print(type(html))
# once response use read() method, response is gone.
# print(resp.read())

from urllib import parse
params = {"v": "EuC-yVzHhMI", "t": "5m56s"}
querystring = parse.urlencode(params)
print(querystring)
url3 = "https://youtube.com/watch" + "?" + querystring
print(url3)
resp = request.urlopen(url3)
print(resp.read().decode("utf-8")[:100])