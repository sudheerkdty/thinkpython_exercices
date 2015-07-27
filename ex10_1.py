def nested_sum(usr_list,newlist = [0]):
	def flist(usr_list):
		"Returns a flat list"
		for i in range(len(usr_list)):
			try:
				if int(usr_list[i]):
					newlist.append(int(usr_list[i]))
				return newlist
			except ValueError:
		
			

	flist(usr_list)
	print sum(newlist)

		
usr_list = list(raw_input('input a list'))
nested_sum(usr_list)
