#Program that accepts a tuple and return its sum
def sum_all(usr_tuple):
	return sum(usr_tuple)

if __name__ == '__main__':
	usr_tuple = tuple(map(int,raw_input('Input a tuple\n').split(',')))
	print sum_all(usr_tuple)
	
