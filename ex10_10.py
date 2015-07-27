#Write a function that reads the file words.txt and builds a list with one element per word.
word = open('a.txt')
def append_method(input_file, t = []):
	for line in input_file:
		word = line.split(' ')
		for i in word:
			if len(i)>1:		
				t.append(i[0])
	return t
def concatination(input_file, t = ''):
	for line in input_file:
		word = line.split(' ')
		for i in word:
			if len(i)>1:		
				t= t + (i[0])
	return t
choice = raw_input('which methord you prefer? \n Choose \n1 for append_method  2 for concatination method(ie,t=t+[x])')
if choice =='1':
	print append_method(word)
elif choice =='2':
	print concatination(word)
