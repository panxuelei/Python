def spam():
	global eggs
	eggs = 'spam change in spam()'

eggs = 'global'
spam()
print(eggs)