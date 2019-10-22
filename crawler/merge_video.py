from moviepy.editor import *
import os
from natsort import natsorted

l = []

# path = "C:\\Users\\Administrator\\Desktop\\渗透测试工程师"
path = "C:\\Users\\Administrator\\Desktop\\临时"
import requests
from bs4 import BeautifulSoup
import re
import os

url = "https://www.bilibili.com/video/av29093363"
headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                          ' AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/70.0.3538.102 Safari/537.36'}
response = requests.get(url, headers=headers)
content = response.text
# print(content)
# soup = BeautifulSoup(content, 'lxml')
# 正则表达式匹配，找到所有课程的名称
pattern = re.compile(r"part\":\"(.*?)\",")
# pattern = re.compile(r"\"part\":\"(.*?)\s.*?\"duration\"")
result = pattern.findall(content, re.S)
# print(result)
# print(len(result))

# 获取每个课程的id
pattern2 = re.compile(r"\"cid\":(\d+),\"page\"")
result2 = pattern2.findall(content, re.S)
# print(result2)
# print(len(result2))
i=0
for title in result:
    print(title+ " " + result2[i])
    i += 1

#
# L = []
# for root, dirs, files in os.walk(path):
#     files = natsorted(files)
#     for file in files:
#         filePath = os.path.join(root, file)
#         merge = VideoFileClip(filePath)
#         print(file)
#         print(len(files))
#
#         L.append(merge)

# files = os.listdir(path)
# files = natsorted(files)
# for video in files:
#     print(video)
#     filePath = path + "\\" + video
#     merge = VideoFileClip(filePath)
#     L.append(video)
#
# final_clip = concatenate_videoclips(L)
# final_clip.to_videofile("./taeget.mp4", fps=24, remove_temp=False)