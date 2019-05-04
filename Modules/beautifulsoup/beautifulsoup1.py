from bs4 import BeautifulSoup
import requests

source = requests.get('https://coreyms.com').text
# print(source)
soup = BeautifulSoup(source, 'lxml')
# article = soup.find('article')
# # print(article.prettify())

for article in soup.find_all('article'):
    headline = article.h2.a.text
    # print(headline)

    summary = article.find('div', class_='entry-content').p.text
    # print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        # print(vid_src)
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        # print(vid_id)
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except:
        yt_link = None

    print(yt_link)
    print()