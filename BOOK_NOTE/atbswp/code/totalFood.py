#下面这个程序使用字典包含其他字典，用于记录谁为野餐带来了什么食物
#totalBrought()函数可以读取这个数字结构，计算每种食物的总数

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
			 'Bob': {'ham sandwiches': 3, 'apples': 2},
			 'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
	numBrought = 0
	for k, v in guests.items():
		numBrought = numBrought + v.get(item, 0)
	return numBrought

print('Number of thing being brought:')
print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apples Pies ' + str(totalBrought(allGuests, 'apple pies')))
