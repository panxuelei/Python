# https://www.geeksforgeeks.org/try-except-python/
# Python code to illustrate working of try()
def divide(x, y):
    try:
        result = x//y
        print('Answer: ', result)
    except ZeroDivisionError:
        print('Sorry! You are dividing by zero.')

divide(3,2)
divide(3,0)

