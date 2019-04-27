
# rasie an exception

# x = 10
# if x>5:
#     raise Exception('x should not exceed 5. The value of x was: {}'.format(x))


# AssertionError Exception

# import sys
# print(sys.platform)
# assert ('win32' in sys.platform), 'This code runs on Windows only.'
# print('hello')
# assert ('linux' in sys.platform), 'This code runs on linux only.'


# try except
import sys

def linux_interaction():
    assert ('win32' in sys.platform), 'Function can only run on ' \
                                      'Windows systems.'
    print('Doing something.')

try:
    linux_interaction()
except:
    print('Windows function was not executed')