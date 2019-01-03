import requests
import re
from bs4 import BeautifulSoup


if __name__ == '__main__':
    url = 'https://ocw.mit.edu/courses/electrica' \
          'l-engineering-and-computer-science/6-006' \
          '-introduction-to-algorithms-fall-2011/'
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                             ' AppleWebKit/537.36 (KHTML, like Gecko)'
                             ' Chrome/70.0.3538.102 Safari/537.36'}
    content = requests.get(url, headers=headers).text
    pattern = re.compile(r'<title>(.*?)</title>')
    print(pattern.findall(content, re.S)[0].split(' | ')[0])

    pattern2 = re.compile(r'<meta content="(.*?)"')
    print(pattern2.findall(content, re.S)[2])