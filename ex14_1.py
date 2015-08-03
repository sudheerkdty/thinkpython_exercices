#program to implement walk
import os
def walk(path):
	for i in os.walk(path):
		return i

if __name__ == '__main__':
#	cwd = raw_input('Enter path')
	cwd = os.getcwd()
	print walk(cwd)
