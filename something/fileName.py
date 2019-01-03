import os

'''
涉及知识：某路径下文件的遍历，文件重命名
'''
# 文件名都是这样的：23.23 复习
# 需要去掉前面三个字符
if __name__ == '__main__':
    path = 'E:\Tutorial\【郝斌】浅显易懂～数据结构入门'
    oldNames = os.listdir(path)
    file_path = path + '\\' # 后面就直接加上文件名就是文件袋绝对路径了
    for oldName in oldNames:
        newName = oldName[3:] # 去掉前三个字符
        # 重命名
        # os.rename() 需要文件的绝对路径，只有文件名不行
        os.rename(file_path+oldName, file_path+newName)