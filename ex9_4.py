#Program to read contents of a file and return words that has only characters entered by user
#This program reads filename  from comandline
from sys import argv
word_no = count_no_e = 0
script,file_name = argv
			
def uses_only(word,letter):
    for char in word:
        if char not in letter:
            return False
    return True  

fin = open(file_name)
count = 0
total = 0.0
letter = raw_input('Please enter letters :\n')
for line in fin:
    lists = line.split()
    for word in lists:
	total += 1
	if uses_only(word, letter):
		count += 1
	        print word

percent = (count / total) * 100

print str(percent) + "% of the words have only the provided letters."
