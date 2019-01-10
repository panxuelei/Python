import requests
from bs4 import BeautifulSoup
import re
import os,errno

# r = requests.get("http://www.pythonscraping.com")
# bs = BeautifulSoup(r.text, 'lxml')
# image = bs.find("a", {"id": "logo"}).find("img")["src"]
# print(image)

def header(referer):
    headers = {
        'Host': 'i.meizitu.net',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': '{}'.format(referer),
    }
    return headers

if __name__ == '__main__':
    '''
    单个post测试
    '''

    # url = 'https://acidimg.cc/img-594d32f20d161.html'
    # url = 'https://imx.to/img-587b1d097e902.html'
    url = 'https://vipergirls.to/threads/2462785-Suji-23-6-2016'
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                             ' AppleWebKit/537.36 (KHTML, like Gecko)'
                             ' Chrome/70.0.3538.102 Safari/537.36'}
    proxies = {
        'https': '127.0.0.1:1080',
        'http': '127.0.0.1:1080'
    }
    content = requests.get(url, headers=headers, proxies=proxies).text
    # picList = re.findall('title=.*?src="(.*?)"', content, re.S)
    # # picList3 = re.findall("class='centred'src='(.*?)'", content, re.S)
    # print(picList)
    # print(content)
    title = re.findall('h2.*?>\n(.*?)\n</h2>', content, re.S)
    folder = 'E:\\vipergirls\\{}'.format(title[0])
    try:
        os.makedirs(folder)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    start = content.index('blockquote')
    stop = content.index('blockquote', start + 1)
    content = content[start:stop]
    pageList = re.findall('a href="(.*?)"', content, re.S)
    # print(pageList)
    print('正在下载: ' + title[0] + '\n' + '共{}张图片:'.format(len(pageList)))
    i = 1
    for page in pageList:
        response = requests.get(page, headers=headers, proxies=proxies)
        content = response.text
        picList = re.findall('title=.*?src="(.*?)"', content, re.S)
        for pic in picList:
            picName = i
            fullPath = folder + '\\' + str(picName) + '.' + pic.split('.')[-1]
            temp = requests.get(pic, proxies=proxies)
            print(str(i), end=' ')
            with open(fullPath, "wb") as f:
                    f.write(temp.content)
            i += 1