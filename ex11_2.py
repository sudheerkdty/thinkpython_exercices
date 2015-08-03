# Program that accepts a file name and store letters and count of each words in a dictionary
file_open =raw_input("enter file name to open:\n")
fin = open('a.txt')

def histogram(word):
	d = dict()
	for c in word:
		 d[c] = 1 + d.get(c, 0)
	return d



def dict_word(fin,count ={}):
	for line in fin: #returns line in file
		word = line.split()# stores words in each line in a list
		for i in word:
			count[i] = histogram(i) #calls histogram function to count characters in current word
	return count

print dict_word(fin)
