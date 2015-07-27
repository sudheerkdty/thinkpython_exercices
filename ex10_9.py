#program that removes duplicates from a user entered list
usr_list = raw_input('enter a list of numbers seperated by commas :\n').split(',')

def remove_duplicates(usr_list,duplicate = []):
	for i in usr_list:
		if not i in duplicate:
			duplicate.append(i)
	return duplicate

print remove_duplicates(usr_list)
