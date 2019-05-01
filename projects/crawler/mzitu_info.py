'''
如果一个文件夹不存在，创建它
#1
if not os.path.exists('mzitu'):
    os.makedirs('mzitu')
#2
try:
    os.makedirs('mzitu')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

获得某个标签下属性的值
soup.img.get('alt')

'''