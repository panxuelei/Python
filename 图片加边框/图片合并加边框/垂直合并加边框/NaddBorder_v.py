from PIL import Image, ImageOps
import os

border1 = 4 #内边框宽度
border2 = 2 #中边框宽度
border3 = 2 #外边框宽度
color1 = "#c00000" #内、外边框颜色
color2 = "white" #中框颜色
result = "垂直合并加边框.jpg" #合并加边框后的图片名称

cwd = os.getcwd()
list_im = []

for file in os.listdir(cwd):
	if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".PNG"):
		list_im.append(file)


imgs = [Image.open(i) for i in list_im]
#寻找最小的长和宽
widths = []
heights = []
for img in imgs:
	widths.append(img.size[0])
	heights.append(img.size[1])

min_width = min(widths)
min_height = min(heights)
#创建合并后的图片大小，不带边框
new_img = Image.new("RGB", (min_width,
					min_height*len(imgs)))

i=0
for img in imgs:
	new_img.paste(imgs[i].resize((min_width, min_height)),
					(0,min_height*i, 
						min_width, min_height*(i+1)))
	i += 1

bimg = ImageOps.expand(new_img, border=border1, fill=color1)
bimg = ImageOps.expand(bimg, border=border2, fill=color2)
bimg = ImageOps.expand(bimg, border=border3, fill=color1)
bimg.save(result)