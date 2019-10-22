#漂亮的打印字典
import pprint
message = 'It was .'
count = {}

for character in message:
	count.setdefault(character, 0)
	count[character] = count[character] + 1

pprint.pprint(count)
#如果希望得到的漂亮打印的文本作为字符串，而不是显示在屏幕上，
#那就调用pprint.pformat().
pprint.pformat(count) #作为字符串，没有任何输出
print(pprint.pformat(count))