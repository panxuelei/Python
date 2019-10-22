'''编写一个函数，它以一个列表值作为参数，返回一个字符串。该字符串包含所
有表项，表项之间以逗号和空格分隔，并在最后一个表项之前插入 and。例如，将
前面的 spam 列表传递给函数，将返回'apples, bananas, tofu, and cats'。'''
spam = ['apples', 'bananas', 'tofu', 'cats']

def temp(spam):
	print('\'', end='')
	for food in spam:
		if spam.index(food) == len(spam)-1:
			print('and ' + food + '\'')
			break
		print(food, end=', ')

temp(spam)