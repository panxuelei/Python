import requests
import os, errno
import re
from bs4 import BeautifulSoup
import urllib.request




# preprocess: url to html content
def preprocess(url):
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                             ' AppleWebKit/537.36 (KHTML, like Gecko)'
                             ' Chrome/70.0.3538.102 Safari/537.36'}
    return requests.get(url, headers=headers).text

# get posts title
def get_posts_title(content):
    pattern = re.compile(r'alt.*?target="_blank">(.*?)</a></span>')
    return pattern.findall(content, re.S)

# get posts link
def get_posts_link(content):
    pattern = re.compile(r'<li><a href="(.*?)" target="_blank"><img width=')
    return pattern.findall(content, re.S)

# get pics link
def get_pics_link(postLink):
    pattern = re.compile(r'class="main-image".*?><img src="(.*?)" alt=')
    pagesList = []
    picsList = []
    # posts every page
    # general url
    # num of pages
    for i in range(1, numsOfPage):
        generalURL = postLink[:28] + '/' + str(i)
        pagesList.append(generalURL)
        picsList.append(pattern.findall(preprocess(generalURL), re.S)[0])

    return picsList

# get nums of page
def get_nums_of_page(postLink):
    pattern = re.compile(r"class='dots'>…</span>.*?<span>(\d+)</span>")

    return int(pattern.findall(preprocess(postLink), re.S)[0])

# save pics
def save_pics(picsList):
    for link in picsList:
        picName = link.split('/')[-1]
        fullPath = 'E:\\NewFolder\\code\\Python\\crawler\\mzitu\\{}{}P'.format(titles[i], numsOfPage) + '\\' + picName
        temp = requests.get(link, headers = {'Referer': link}) #反盗链设置，简单的做法
        # with open(fullPath, "wb") as f:
        #     f.write(temp.content)

if __name__ == '__main__':
    url = "https://www.mzitu.com"
    content = preprocess(url)
    # print(get_posts_title(content))
    postsLink = get_posts_link(content)
    i = 0
    for postLink in postsLink:
        numsOfPage = get_nums_of_page(postLink)
        titles = get_posts_title(content)
        outPath = "./mzitu/{}".format(titles[i])
        print('正在下载：\n' + titles[i] + '......')
        print('共{}张图片'.format(numsOfPage))
        # if main output folder not exist, create it
        try:
            os.makedirs(outPath)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        picsList = get_pics_link(postLink)
        save_pics(picsList)
        i += 1

