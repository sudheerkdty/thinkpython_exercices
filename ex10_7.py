# Program that accepts two words and check for anagram
word1 = raw_input('Enter word1:\n')
word2 = raw_input('Enter word2:\n')

def is_anagram(word1,word2):
	a = list(word1)
	b = list(word2)
	if a.sort() == b.sort():
		return True
	else:
		return False

result = is_anagram(word1,word2)
print "Is anagram? ",result
