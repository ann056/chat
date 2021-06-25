def read_file(filename):
	chat = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			chat.append(line.strip())
	return chat

def convert(chat):
	allen_words = 0
	allen_stickers = 0
	allen_pic = 0
	viki_words = 0
	viki_stickers = 0
	viki_pic = 0
	for line in chat:
		s = line.split(' ') # split本身自己就會變成清單
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_stickers += 1
			elif s[2] == '圖片':
				allen_pic += 1
			else:
				for m in s[2:]:
					allen_words += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_stickers += 1
			elif s[2] == '圖片':
				viki_pic += 1
			else:
				for m in s[2:]:
					viki_words += len(m)
	print('Allen說了', allen_words, '個字')
	print('Allen傳了', allen_stickers, '個貼圖')
	print('Allen傳了', allen_pic, '張照片')
	print('Viki說了', viki_words, '個字')
	print('Viki傳了', viki_stickers, '個貼圖')
	print('Viki傳了', viki_pic, '張照片')


def main():
	chat = read_file('LINE-Viki.txt')
	convert(chat)


main()





