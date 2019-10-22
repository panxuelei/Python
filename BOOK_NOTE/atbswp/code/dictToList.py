#如何从一个词典中得到一个列表
#spam.keys() --->  dict_keys(['color', 'age'])
spam = {'color': 'red', 'age': 42}
print(list(spam.keys()))

#将键和值赋值给不同的变量
for k, v in spam.items():
	print('Key: ' + k + ' Value: ' + str(v))