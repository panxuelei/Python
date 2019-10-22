#计算字符串中每个字符出现的次数

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
	count.setdefault(character, 0)
	count[character] = count[character] + 1

print(count)