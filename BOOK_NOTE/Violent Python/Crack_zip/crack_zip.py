# 简单的破解zip压缩文件的代码
# 知识点：1.zipfile库 2.文件处理 3.多线程 4.optparse库
# 还未实现：1.多线程 2.optparse库，命令行指定zip文件和字典文件
import zipfile

# 测试解压密码的函数
def extractFile(zFile, password):
	try:
		zFile.extractall(path = extract_to, pwd=bytes(password, 'utf-8'))
		return True
	except:
		return False

def main():
	zFile = zipfile.ZipFile(file_name)
	with open('dictionary.txt', 'r') as dictionary:
		for line in dictionary.readlines():
			password = line.strip('\n')
			# print(line)
			ok = extractFile(zFile, password)
			if ok:
				print('Password!!!!----->', password)
				exit(0)


if __name__ == '__main__':
	# 要破解的文件
	file_name = 'password1234.zip'
	# 输出文件夹（就是去掉'.zip'而已）
	extract_to = file_name.split('.')[0]
	main()