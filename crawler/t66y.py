import requests
import re
import os
import errno
from time import sleep


if __name__ == '__main__':
    url_list = [

                ]

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                             ' AppleWebKit/537.36 (KHTML, like Gecko)'
                             ' Chrome/70.0.3538.102 Safari/537.36'}
    proxies = {
        'https': '127.0.0.1:1080',
        'http': '127.0.0.1:1080'
    }

    for url in url_list:
        response = requests.get(url, proxies=proxies)
        response.encoding=('GBK')
        content = response.text
        # print(content)
        # 匹配方案1
        picList = re.findall("data-src='(.*?)'", content, re.S)
        # 匹配方案2，有些帖子并不是上面这种格式
        picList2 = re.findall("input src='(.*?)'", content, re.S)
        picList
        if len(picList) == 0: picList = picList2
        # print(pic_url)
        # print(len(picList))
        title = re.findall('<h4>(.*?)</h4>', content, re.S)
        # print(title)
        print('正在下载: ' + title[0])
        outPath = "C:\\Users\\Aaron Swartz\\Desktop\\{}".format(title[0])
        try:
            os.makedirs(outPath)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        i = 1
        for pic in picList:
            try:
                picName = pic.split('/')[-1]
                fullPath = outPath + '\\' + picName
                temp = requests.get(pic, proxies=proxies)
                print(str(i) + ' ', end='')
                with open(fullPath, "wb") as f:
                    f.write(temp.content)
            except requests.exceptions.ConnectionError:
                print(str(i) + "'s pic failed")

            i += 1

        print('\n')