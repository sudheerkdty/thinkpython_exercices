word = raw_input('Enter a word to check palindrome or not : \n')
print '%s is Palindrome ? \n'%(word),
print word == word[::-1]
