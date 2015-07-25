word = raw_input('Enter a Word : ')
char = raw_input('Enter search Character : ')
def count(word,char):
	count = 0
	for letter in word:
		if letter == char:
			count = count + 1
	return count
char_count = count(word,char)
print char_count
