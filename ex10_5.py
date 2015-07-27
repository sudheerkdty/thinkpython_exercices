#function thath takes a list and returns its middle
def chop(usr_list):
	for i in usr_list:
		if len(usr_list)>1:
			print "removing"		
			print usr_list.pop(0) #pop first element
			print usr_list.pop(-1) #pop last element
			
	print usr_list.pop(0) #pop remaining element
	return usr_list

usr_list = raw_input('enter a list of numbers seperated by commas :\n').split(',')
print "The list you've entered is: \n", usr_list
print chop(usr_list)
