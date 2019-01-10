spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

spam = ['ants', 'cats', 'dogs', 'badgers']
spam.sort()
print(spam)

spam.sort(reverse=True)
print(spam)

spam = ['Alice', 'ants', 'Bob', 'Carol']
spam.sort()
print(spam)

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)

