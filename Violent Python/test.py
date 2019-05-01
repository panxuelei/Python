# https://blog.csdn.net/Big_talent/article/details/52367184
# https://blog.csdn.net/q1w2e3r4470/article/details/51859467
# 记得重启系统

from unrar import  rarfile

dictionary = 'E:\\NewFolder\\code\\Python\\Violent Python\\Crack_zip\\dictionary.txt'
file = 'F:\\BaiduNetdiskDownload\\NYXG.rar'
extract_to = 'F:\\BaiduNetdiskDownload'
rar = rarfile.RarFile(file)

with open(dictionary, 'r') as p:
    p = p.readlines()
    for password in p:
        password = password.strip('\n')
        # print(password)
        if(rar.extractall(path=extract_to,pwd='www.97tv.club')):
            break
        else:
            continue

