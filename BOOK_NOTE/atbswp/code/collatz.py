'''
编写一个名为 collatz()的函数，它有一个名为 number 的参数。如果参数是偶数，
那么 collatz()就打印出 number // 2，并返回该值。如果 number 是奇数，collatz()就打
印并返回 3 * number + 1。
然后编写一个程序，让用户输入一个整数，并不断对这个数调用 collatz()，直
到函数返回值１'''
'''
在前面的项目中添加 try 和 except 语句，检测用户是否输入了一个非整数的字
符串。正常情况下，int()函数在传入一个非整数字符串时，会产生 ValueError 错误，
比如 int('puppy')。在 except 子句中，向用户输出一条信息，告诉他们必须输入一个
整数。'''

def collatz(number):
	if number%2 == 0:
		number = number//2
		print(number)
	else:
		number = 3*number + 1
		print(number)
	return number


spam = input('Please input a number:')

try:
	spam = int(spam)
	while spam != 1:
		spam = collatz(spam)

	print('Now, the value of spam is ' + str(spam))
	
except ValueError:
	print('Sorry, you must type a number.')
