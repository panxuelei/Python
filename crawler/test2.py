import re
import requests
import os, errno

if __name__ == '__main__':
    urls = [
            'https://vipergirls.to/threads/2886593-Sua-19-01-2016-34x'
            ]

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                             ' AppleWebKit/537.36 (KHTML, like Gecko)'
                             ' Chrome/70.0.3538.102 Safari/537.36'}
    proxies = {
        'https': '127.0.0.1:1080',
        'http': '127.0.0.1:1080'
    }
    # 有多少个url不是静态页面的计数变量
    count = 0
    for url in urls:
        response = requests.get(url, headers=headers, proxies=proxies)
        content = response.text
        # 套图的标题
        title = re.findall('h2.*?>\n(.*?)\n</h2>', content, re.S)

        start = content.index('blockquote')
        stop = content.index('blockquote', start + 1)
        content = content[start:stop]
        pageList = re.findall('a href="(.*?)"', content, re.S)

        # 拿第一链接做测试，如果是静态页面就开始下载，否则，将链接添加到 others.txt, 并开始下一轮循环
        response2 = requests.get(pageList[0], headers=headers, proxies=proxies)
        content2 = response2.text
            # 其实pic列表也就一个元素，每个页面一个图片
        pic = re.findall('title=.*?src="(.*?)"', content2, re.S)
        if len(pic) > 0:
            # 此url是静态页面

            # 如果文件夹不存在创建文件夹
            title[0] = '【{}P】'.format(len(pageList)) + title[0]
            print('\n正在下载: ' + title[0] + '\n' + '共{}张图片:'.format(len(pageList)))
            folder ='E:\\vipergirls\\{}'.format(title[0])
            if not os.path.exists(folder):
                os.makedirs(folder)

            i = 1
            # 开始下载图片
            for page in pageList:
                picName = i
                fullPath = folder + '\\' + str(picName) + '.' + pic[0].split('.')[-1]
                # 正在下载第几张图片
                print(str(i), end=' ')
                # 如果图片不存在的话就下载，防止重复下载
                if not os.path.exists(fullPath):
                    response3 = requests.get(page, headers=headers, proxies=proxies)
                    content3 = response3.text
                    # 图片链接，只有一个元素的列表
                    pic = re.findall('title=.*?src="(.*?)"', content3, re.S)
                    # 保存图片
                    response4 = requests.get(pic[0], headers=headers, proxies=proxies)
                    with open(fullPath, "wb") as f:
                        f.write(response4.content)
                    i += 1
                else:
                    print('图片已存在')
                    i += 1
                    continue

        # 不是静态页面，另做处理
        else:
            count += 1
            print('例外!' + url)
            others = open('others.txt', 'a')
            others.write(url+'\n')
            print('已添加至 others.txt')
            continue

    print('总共{}组套图，已下载{}组，有{}组例外，保存在others.txt文件中'.format(len(urls), len(urls)-count, count))



