#"""Program to print names of Ducklings using suffix 'ack' and prefix 'JKLMNOPQ'"""

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
	if letter == 'O' or letter == 'Q': 
		print  letter +'u'+ suffix
	else:
		print  letter + suffix
	
