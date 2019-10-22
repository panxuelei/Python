spam = {'name': 'Pooka', 'age': 5}
print(spam.setdefault('color', 'black'))
print(spam)
print(spam.setdefault('color', 'white'))
print(spam)