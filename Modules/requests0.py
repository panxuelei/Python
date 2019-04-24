import requests

url0 = 'https://xkcd.com/353'

r0 = requests.get(url0)

# print(r0)

# content: Content of the response, in bytes.
# print(r.content) # for picture

# text: Content of the response, in unicode.
# print(r.text)

url1 = 'https://imgs.xkcd.com/comics/python.png'
r1 = requests.get(url1)

print(r1.status_code)
print(r1.ok)
print(r1.headers)

# print(r1.content) # print image in bytes

# save the picture
# with open('requests0.png', 'wb') as f:
#     f.write(r1.content)


