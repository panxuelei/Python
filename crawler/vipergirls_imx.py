import re
import requests
import os, errno

if __name__ == '__main__':
    urls = [
            'https://vipergirls.to/threads/2462785-Suji-23-6-2016',
            'https://vipergirls.to/threads/2878491-Sua-07-05-2015-31x',
            'https://vipergirls.to/threads/2886593-Sua-19-01-2016-34x',
            'https://vipergirls.to/threads/2889477-Sua-14-03-2016-50x',
            'https://vipergirls.to/threads/2467726-Sejin-30-6-2016',
            'https://vipergirls.to/threads/2486340-Yeni-16-7-2016',
            'https://vipergirls.to/threads/2881970-Suji-21-05-2015-30x',
            'https://vipergirls.to/threads/2650707-Yeni-23-8-2016',
            'https://vipergirls.to/threads/2878497-Sua-07-05-2015-32x',
            'https://vipergirls.to/threads/2876026-Sejin-05-05-2015-32x',
            'https://vipergirls.to/threads/2550247-Sua-30-7-2016',
            'https://vipergirls.to/threads/2650363-Gyuri-20-8-2016',
            'https://vipergirls.to/threads/2478555-Dohui-12-7-2016',
            'https://vipergirls.to/threads/2889476-Sua-07-03-2016-51x',
            'https://vipergirls.to/threads/2466282-Dohui-30-6-2016',
            'https://vipergirls.to/threads/2874217-Dayeong-06-02-2016-63x',
            'https://vipergirls.to/threads/2876906-Sejin-04-03-2016-43x',
            'https://vipergirls.to/threads/2478563-Sejin-12-7-2016',
            'https://vipergirls.to/threads/2881965-Suji-06-05-2015-31x',
            'https://vipergirls.to/threads/2875161-Mina-31-12-2015-37x',
            'https://vipergirls.to/threads/2881898-Suji-06-05-2015-30x',
            'https://vipergirls.to/threads/2462744-Jiyeong-22-6-2016',
            'https://vipergirls.to/threads/2550246-Jiwon-30-7-2016',
            'https://vipergirls.to/threads/2467745-Seohui-2-7-2016',
            'https://vipergirls.to/threads/2884463-Suji-05-03-2016-31x',
            'https://vipergirls.to/threads/2470895-Yeni-6-7-2016',
            'https://vipergirls.to/threads/2883294-Suji-09-12-2015-51x',
            'https://vipergirls.to/threads/2466234-Chaeyeong-29-6-2016',
            'https://vipergirls.to/threads/2887119-Sua-01-03-2016-69x',
            'https://vipergirls.to/threads/2881043-Suyeon-09-05-2015-36x',
            'https://vipergirls.to/threads/2893024-Jiyeong-04-02-2016-60x',
            'https://vipergirls.to/threads/2500172-Sua-20-7-2016',
            'https://vipergirls.to/threads/2887113-Sua-01-02-2016-56x',
            'https://vipergirls.to/threads/2881945-Suji-06-05-2015-30x',
            'https://vipergirls.to/threads/2879504-Sua-07-05-2015-30x',
            'https://vipergirls.to/threads/2875565-Seohui-18-03-2016-51x',
            'https://vipergirls.to/threads/2889706-Iel-09-03-2016-45x',
            'https://vipergirls.to/threads/2650707-Yeni-23-8-2016',
            'https://vipergirls.to/threads/2884855-Sua-23-09-2015-30x',
            'https://vipergirls.to/threads/2876738-Sejin-03-02-2016-69x',
            'https://vipergirls.to/threads/2500169-Jiwon-20-7-2016',
            'https://vipergirls.to/threads/2884851-Sua-12-08-2015-30x',
            'https://vipergirls.to/threads/2889701-Iel-29-02-2016-52x',
            'https://vipergirls.to/threads/2884458-Suji-11-02-2016-30x',
            'https://vipergirls.to/threads/2883290-Suji-06-11-2015-49x',
            'https://vipergirls.to/threads/2876029-Sejin-01-12-2015-35x',
            'https://vipergirls.to/threads/2893029-Jiyeong-16-02-2016-43x',
            'https://vipergirls.to/threads/2467726-Sejin-30-6-2016',
            'https://vipergirls.to/threads/2478608-Seohui-13-7-2016',
            'https://vipergirls.to/threads/2889711-Iel-30-03-2016-46x',
            'https://vipergirls.to/threads/2883294-Suji-09-12-2015-51x',
            'https://vipergirls.to/threads/2650454-Dohui-22-8-2016',
            'https://vipergirls.to/threads/2879501-Sua-07-05-2015-30x',
            'https://vipergirls.to/threads/2876906-Sejin-04-03-2016-43x',
            'https://vipergirls.to/threads/2885856-Sua-26-11-2015-32x',
            'https://vipergirls.to/threads/2650363-Gyuri-20-8-2016',
            'https://vipergirls.to/threads/2881970-Suji-21-05-2015-30x',
            'https://vipergirls.to/threads/2879456-Sua-07-05-2015-30x',
            'https://vipergirls.to/threads/2884858-Sua-04-11-2015-51x',
            'https://vipergirls.to/threads/2876910-Sejin-21-03-2016-48x',
            'https://vipergirls.to/threads/2889482-Sua-05-04-2016-35x',
            'https://vipergirls.to/threads/2876683-Sejin-25-01-2016-56x',
            'https://vipergirls.to/threads/2881969-Suji-06-05-2015-30x',
            'https://vipergirls.to/threads/2876908-Sejin-14-03-2016-49x',
            'https://vipergirls.to/threads/2884417-Suji-23-12-2015-43x',
            'https://vipergirls.to/threads/2893021-Jiyeong-26-01-2016-62x',
            'https://vipergirls.to/threads/2874199-Dayeong-03-05-2015-33x',
            'https://vipergirls.to/threads/2885893-Sua-28-12-2015-57x',
            'https://vipergirls.to/threads/2523058-Suji-26-7-2016',
            'https://vipergirls.to/threads/2586091-Sejin-11-8-2016',
            'https://vipergirls.to/threads/2881034-Sua-30-07-2015-33x',
            'https://vipergirls.to/threads/2889705-Iel-04-03-2016-47x',
            'https://vipergirls.to/threads/2583171-Gyuri-10-8-2016',
            'https://vipergirls.to/threads/2884454-Suji-04-01-2016-47x',
            'https://vipergirls.to/threads/2876682-Sejin-18-01-2016-68x',
            'https://vipergirls.to/threads/2874222-Dayeong-12-03-2016-63x',
            'https://vipergirls.to/threads/2875565-Seohui-18-03-2016-51x',
            'https://vipergirls.to/threads/2874186-Gyuri-12-01-2016-60x',
            'https://vipergirls.to/threads/2884856-Sua-28-10-2015-41x',
            'https://vipergirls.to/threads/2518254-Yewon-25-7-2016',
            'https://vipergirls.to/threads/2462740-Sejin-20-6-2016',
            'https://vipergirls.to/threads/2887114-Sua-10-02-2016-48x',
            'https://vipergirls.to/threads/2874136-Gyuri-30-11-2015-42x',
            'https://vipergirls.to/threads/2586091-Sejin-11-8-2016',
            'https://vipergirls.to/threads/2874204-Dayeong-03-05-2015-28x',
            'https://vipergirls.to/threads/2876683-Sejin-25-01-2016-56x',
            'https://vipergirls.to/threads/2884852-Sua-18-08-2015-31x',
            'https://vipergirls.to/threads/2886601-Sua-27-01-2016-54x',
            'https://vipergirls.to/threads/2550247-Sua-30-7-2016',
            'https://vipergirls.to/threads/2887119-Sua-01-03-2016-69x',
            'https://vipergirls.to/threads/2874187-Gyuri-15-03-2016-60x',
            'https://vipergirls.to/threads/2893035-Hera-19-12-2015-36x',
            'https://vipergirls.to/threads/2887118-Sua-24-02-2016-51x',
            'https://vipergirls.to/threads/2889710-Iel-25-03-2016-43x',
            'https://vipergirls.to/threads/2874214-Dayeong-02-01-2016-51x',
            'https://vipergirls.to/threads/2881025-Sua-02-07-2015-25x',
            'https://vipergirls.to/threads/2884462-Suji-29-02-2016-56x',
            'https://vipergirls.to/threads/2886592-Sua-06-01-2016-67x',
            'https://vipergirls.to/threads/2462731-Sua-17-6-2016',
            'https://vipergirls.to/threads/2889706-Iel-09-03-2016-45x',
            'https://vipergirls.to/threads/2467750-Jiyeong-4-7-2016',
            'https://vipergirls.to/threads/2523063-Dayeong-28-7-2016',
            'https://vipergirls.to/threads/2889707-Iel-18-03-2016-60x',
            'https://vipergirls.to/threads/2879505-Sua-07-05-2015-33x',
            'https://vipergirls.to/threads/2889476-Sua-07-03-2016-51x',
            'https://vipergirls.to/threads/2874221-Dayeong-27-02-2016-33x',
            'https://vipergirls.to/threads/2875163-Mina-14-01-2016-64x',
            'https://vipergirls.to/threads/2884464-Suji-26-03-2016-53x',
            'https://vipergirls.to/threads/2876910-Sejin-21-03-2016-48x',
            'https://vipergirls.to/threads/2881022-Sua-02-07-2015-25x',
            'https://vipergirls.to/threads/2462740-Sejin-20-6-2016',
            'https://vipergirls.to/threads/2883291-Suji-05-12-2015-34x',
            'https://vipergirls.to/threads/2467745-Seohui-2-7-2016',
            'https://vipergirls.to/threads/2884416-Suji-21-12-2015-43x',
            'https://vipergirls.to/threads/2588829-Dohui-12-8-2016'
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
        response = requests.get(url, headers=headers)
        content = response.text
        # 套图的标题
        title = re.findall('h2.*?>\n(.*?)\n</h2>', content, re.S)

        start = content.index('blockquote')
        stop = content.index('blockquote', start + 1)
        content = content[start:stop]
        pageList = re.findall('a href="(.*?)"', content, re.S)

        # 拿第一链接做测试，如果是静态页面就开始下载，否则，将链接添加到 others.txt, 并开始下一轮循环
        response2 = requests.get(pageList[0], headers=headers)
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
                try:
                    if not os.path.exists(fullPath):
                        response3 = requests.get(page, headers=headers)
                        content3 = response3.text
                        # 图片链接，只有一个元素的列表
                        pic = re.findall('title=.*?src="(.*?)"', content3, re.S)
                        # 保存图片
                        response4 = requests.get(pic[0], headers=headers)
                        with open(fullPath, "wb") as f:
                            f.write(response4.content)
                        i += 1
                    else:
                        print('图片已存在')
                        i += 1
                        continue
                except ConnectionError: # 老是出现下载错误，但是这个网站好像不用代理就可以
                    print("Raise ConnectionError(e, request=request)"
                          " (Caused by ProxyError('Cannot connect to proxy.")
                    others = open('FailedDownload.txt', 'a')
                    others.write(url + '\n')
                    print('已添加至 FailedDownload.txt')
                    i += 1
                    continue
                except:
                    print('Other problem occured!')
                    others = open('FailedDownload.txt', 'a')
                    others.write(url + '\n')
                    print('已添加至 FailedDownload.txt')
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



