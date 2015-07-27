# Program to accept a string and return capitalized string

def capitalize(usr_list,newlist =[]):
	for s in usr_list:
		newlist.append(s.capitalize())
	delimiter = ''
	print delimiter.join(newlist)

	
usr_list = list(raw_input('input a list to capitalize:\n'))
capitalize(usr_list)
