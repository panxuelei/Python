import requests
import re



if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=HtSuA80QTyo&list=' \
          'PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=2'
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                             ' AppleWebKit/537.36 (KHTML, like Gecko)'
                             ' Chrome/70.0.3538.102 Safari/537.36'}
    proxies = {
        'https': '127.0.0.1:1080'
    }
    content = requests.get(url, headers=headers, proxies=proxies).text
    pattern = re.compile(r'ytInitialData*?"title":{"simpleText":"(.*?)"},"longBylineText"')
    print(pattern.findall(content, re.S))