#Program to read contents of a file and print words lengthier than 20 characters
#This program reads filename from comandline
from sys import argv
script,file_name = argv
def printwords(fin):
	for line in fin:
		word = line.split()
		for string in word:
			if len(string)>19:
				print string 

fin = open(file_name)
printwords(fin)
