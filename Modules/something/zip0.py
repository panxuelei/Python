#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-04-27 13:13
# @Author  : Xuelei Pan
# @FileName: zip0.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：
# @Related Links:

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : ${DATE} ${TIME}
# @Author  : Xuelei Pan
# @FileName: ${NAME}.py
# @Eamil   : 317118173pxl@gmail.com
# @Description：
# @Related Links:

x = [1,2,3,4]
y = [7,6,2,1]
z = ['a', 'b', 'c ', 'd']

# for a, b in zip(x,y):
#     print(a,b)

# print(dict(zip(x,y)))
# print()
#
# for i in zip(x,y,z):
#     print(i)

[print(a,b,c) for a,b,c in zip(x,y,z)]

