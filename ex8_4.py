#Program to find a letter in word

print "Enter a word, letter you want to find and index from where you wish to search"
word = raw_input('Word\n>>>')
letter = raw_input('Letter\n>>>')
index = int(raw_input('Index\n>>>'))

def find(word, letter, index):
	while index < len(word):
		if word[index] == letter:
			 print 'found at %d' %index
		
		index = index+1
	
	return-1
find(word, letter, index)
