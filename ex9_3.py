#Program to read contents of a file and return true if word has no forbidden characters entered by user
#This program reads filename  from comandline
from sys import argv
word_no = count_no_e = 0
script,file_name = argv
			
def avoids(word,letter):
    for char in word:
        if char in letter:
            return False
    return True  

fin = open(file_name)
count = 0
total = 0.0
letter = raw_input('Please enter letters to exclude?')
for line in fin:
    lists = line.split()
    for word in lists:
	total += 1
	if avoids(word, letter):
		count += 1
	        print word

percent = (count / total) * 100

print str(percent) + "% of the words don't have the provided letters."
