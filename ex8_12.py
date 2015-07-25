word = raw_input('Enter a word to rotate : ')
para = int(raw_input('Enter the parameter for rotation : '))

for i in word:
	asci =ord(i)
	rotate = asci + para
	print chr(rotate),

