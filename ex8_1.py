"""Program that accepts a word and print each character in seperate line in reverse order"""
word = raw_input('Enter a word:\n>>>')

def rev_word(word):
	index = len(word)-1
	while index >= 0:
		letter = word[index]
		print letter
		index -= 1

rev_word(word)
