# https://www.youtube.com/watch?v=ng2o98k983k
from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# print(soup)
# print(soup.prettify())

# match = soup.title
# print(match)
# match = soup.title.text
# print(match)

# # find div with class atrribute footer
# # find return the first one it found.
# match = soup.find('div', class_='article')
# # print(match)
# headline = match.h2.a.text
# print(headline)
# summary = match.p.text
# print(summary)

# find_all()
for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)
    summary = article.p.text
    print(summary)
    print()
