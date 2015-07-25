#Program to read contents of a file and return true if word has no 'e'
#This program reads filename from comandline
from sys import argv
word_no = count_no_e = 0
script,file_name = argv
			
def has_no_e(word):
    for char in word:
        if char in 'Ee':
            return False
    return True  

fin = open(file_name)
count = 0
total = 0.0
for line in fin:
    lists = line.split()
    for word in lists:
	total += 1
	if has_no_e(word):
		count += 1
	        print word

percent = (count / total) * 100

print str(percent) + "% of the words don't have an 'e'."
