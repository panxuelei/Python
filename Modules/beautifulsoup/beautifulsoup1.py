from bs4 import BeautifulSoup
import requests

source = requests.get('https://coreyms.com').text
# print(source)
soup = BeautifulSoup(source, 'lxml')
article = soup.find('article')
# print(article.prettify())

# headline = article.h2.a.text
# print(headline)

summary = article.find('div', class_='entry-content').p.text
print(summary)