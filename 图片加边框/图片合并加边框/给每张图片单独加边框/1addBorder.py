from PIL import Image, ImageOps
import os

border1 = 10 #内边框宽度
border2 = 6 #中
border3 = 6 #外
color1 = "#c00000" #内、外框颜色
color2 = "white" #中框颜色

cwd = os.getcwd()
for file in os.listdir(cwd):
	if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".PNG"):
		img = Image.open(file)
		bimg = ImageOps.expand(img, border=border1, fill=color1)
		bimg = ImageOps.expand(bimg, border=border2, fill=color2)
		bimg = ImageOps.expand(bimg, border=border3, fill=color1)
		bimg.save("new_"+file)
