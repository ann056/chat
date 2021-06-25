def read_file(filename):
	with open(filename, 'r', encoding='utf-8-sig') as f:
		chat = [] #只是用來把檔案裝進來的清單
		for line in f:
			chat.append(line.strip())
	return chat

def convert(chat):
	new = [] # 用來分類的清單
	people = None
	for line in chat:
		if line == 'Allen':
			people = 'Allen'
			continue
		elif line == 'Tom':
			people = 'Tom'
			continue
		if people:
			new.append(people + ':' + line + '\n')
	return new

def write_file(filename, new):
	with open(filename, 'w') as f:
		for line in new:
			f.write(line)

def main():
	chat = read_file('input.txt')
	new = convert(chat)
	write_file('output.txt', new)

main()





