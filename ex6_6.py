word = raw_input('enter a word to check palindrome:\n')

def palindrome(word):
	rev = reversed(word)
	print "Palindrome : ",
	print list(word) == list(rev)

palindrome(word) 
