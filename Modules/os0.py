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
# os.rename('temp.py', 'test.py')

# # infomation of a file
# print(os.stat('test.py'))
# print(os.stat('test.py').st_size)
#
# from datetime import datetime
# mod_time = os.stat('test.py').st_mtime
# print(datetime.fromtimestamp(mod_time))

# path = 'C:\\Users\\Aaron Swartz\\Desktop\\New folder'
# for dirpath, dirnames, filenames in os.walk(path):
#     print('Current path: ', dirpath)
#     print('Directories: ', dirnames)
#     print('Files: ', filenames)

print(os.environ.get('PATH').split(';')[0])
print(os.path.exists('temp\\temp.txt'))
print(os.path.isdir(os.environ.get('PATH').split(';')[0]))