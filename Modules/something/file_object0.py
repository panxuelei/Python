# File Objects
# https://www.youtube.com/watch?v=Uh2ebFW8OYM

f = open('test0.txt', 'r')

# print(f.name)
# print(f.mode)
f.close()

with open('test0.txt', 'r') as f:
    # # all the content
    # f_contents0 = f.read()
    #
    # # all single line(with '\n' at the end) as element in a list
    # f_contents1 = f.readlines()
    #
    # # just one line, one by one.
    # f_contents2 = f.readline()
    # # use end='' because it automatic return a new line
    # # print(f_contents2)
    # print(f_contents2, end='')
    # f_contents2 = f.readline()
    # print(f_contents2, end='')
    #
    # # readline() and readlines read all content to the memory,
    # # this will cost a lot of memory.
    # # use for loop, read only one line each time to the memory.
    # for line in f:
    #     print(line, end='')

    # # read centern size of content
    # # '\n' also take a space
    # size_to_read = 3
    # f_contents = f.read(size_to_read)
    # while len(f_contents) > 0:
    #     print(f_contents, end='--')
    #     f_contents = f.read(size_to_read)

    # # Create a new file 'test1.txt'
    # with open('test1.txt', 'w') as f:
    #     f.write('Test')
    #     f.write('Test')
    #     f.seek(1)
    #     f.write('X')

    # # copy one file's content to another file
    # with open('test0.txt', 'r') as rf:
    #     with open('test0_copy.txt', 'w') as wf:
    #         for line in rf:
    #             wf.write(line)

    # copy a picture
    with open('wallpaper0.jpg', 'rb') as rf:
        with open('wallpaper0_copy.jpg', 'wb') as wf:
            chunk_size = 4096
            rf_chunk = rf.read(chunk_size)
            while len(rf_chunk) > 0:
                wf.write(rf_chunk)
                rf_chunk = rf.read(chunk_size)




# print(f.closed)
# print(f.read())