import requests
from bs4 import BeautifulSoup
import re
import os

url = "https://www.bilibili.com/video/av32792056"
headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                          ' AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/70.0.3538.102 Safari/537.36'}
response = requests.get(url, headers=headers)
content = response.text
# print(content)
# soup = BeautifulSoup(content, 'lxml')
# 正则表达式匹配，找到所有课程的名称
pattern = re.compile(r"\"part\":\"(.*?)\s.*?\"duration\"")
result = pattern.findall(content, re.S)
i = 0
for title in result:
    # 去掉课程名称中【录像】这几个字
    result[i] = title[0:4] + ' ' + title[8:]
    i += 1
# print(result)
# print(len(result))

# 获取每个课程的id
pattern2 = re.compile(r"\"cid\":(\d+),\"page\"")
result2 = pattern2.findall(content, re.S)
# print(result2)
# print(result2.index('57395723'))
# print(result2)
# print(len(result2))

# 下载的视频文件夹
path = "C:\\Users\\Administrator\\Desktop\\第五版软件考试网络工程师视频教程"
# print(path)
# 视频列表
# v_list = []
for video in os.listdir(path):
    # v_list.append(video)
    if video[:8] in result2:
        # 先用index方法获得当前视频应该有的名称
        # 重命名时，名称要用绝对路径
        new_name = path + "\\" + result[result2.index(video[:8])] + ".flv" # 新名字
        video = path + "\\" + video
        os.rename(video, new_name)

# print(v_list)