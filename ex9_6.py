#Program to read contents of a file and return words that are in alphabetic order
#This program reads filename  from comandline
from sys import argv
word_no = count_no_e = 0
script,file_name = argv
			
def abracadabra(word):
	i = 0
	while i<len(word)-1:
		if word[i+1] < word[i]:
			return False
		i = i + 1
	return True

fin = open(file_name)
count = 0
total = 0.0
for line in fin:
    lists = line.split()
    for word in lists:
	total += 1
	if abracadabra(word):
		count += 1
	        print word

percent = (count / total) * 100

print str(percent) + "% of the words that are in alphabetical order"
