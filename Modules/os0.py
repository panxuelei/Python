import os

# print(os.getcwd())
# print(os.listdir())

# create a folder
# os.mkdir('OS-Demo0')
# os.rmdir('OS-Demo0')

# create a series folder
# os.makedirs('OS-Demo1/Sub-Dir0')
# os.removedirs('OS-Demo1/Sub-Dir0')

# rename(old, new)
os.rename('test.py', 'temp.py')

# infomation of a file
print(os.stat('temp.py'))


print(os.listdir())
