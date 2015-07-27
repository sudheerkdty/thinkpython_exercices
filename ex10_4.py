#function thath takes a list and returns its middle
def middle(usr_list):
	if len(usr_list)>1:
		del usr_list[0]
		del usr_list[-1]
	else:
		usr_list = None
	print "Middle list is :"
	return usr_list

usr_list = raw_input('enter a list of numbers seperated by commas :\n').split(',')
print "The list you've entered is: \n", usr_list
print middle(usr_list)
