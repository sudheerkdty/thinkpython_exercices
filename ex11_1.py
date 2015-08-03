# Program that accepts a file name and store its words in a dictionary
file_open =raw_input("enter file name to open:\n")
fin = open('a.txt')

def dict_word(fin,usr_dict ={}):
	for line in fin: #returns line in file
		word = line.split()# stores words in each line in a list
		for i in word:
			usr_dict[i] = 'test value' #stores words of list as key of dict with value 'test value'
	return usr_dict

print dict_word(fin)
