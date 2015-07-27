#Birthday  Program 
import random
def has_duplicates(usr_list,duplicate = []):
	for i in usr_list:
		if i in duplicate:
			return True
		else:
			duplicate.append(i)
	return False

def random_bdays(n):
	"""Returns a list of integers between 1 and 365, with length (n)."""
	t = []
	for i in range(n):
		bday = random.randint(1, 365)
		t.append(bday)
	return t
def count_matches(students,samples):
	count = 0
	for i in range(samples):
		t = random_bdays(students)
		if has_duplicates(t):
			count += 1
	return count


"""run the birthday simulation 1000 times and print the number of matches"""
num_students = 23
num_simulations = 1000
count = count_matches(num_students, num_simulations)

print 'After %d simulations' % num_simulations
print 'with %d students' % num_students
print 'there were %d simulations with at least one match' % count
