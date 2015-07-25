#Program to find the count of character inside a given word
word = raw_input('Enter a Word : \n')
char = raw_input('Enter search Character : \n')
index = int(raw_input('Enter the index from where you want to search:\n'))

def count(word,char,index):
	count = 0
	while index < len(word):
		if word[index] == char:
			count = count + 1
		index += 1
	return count

char_count = count(word,char,index)
print char_count
