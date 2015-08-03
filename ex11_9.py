#Program to check duplicates
SAMPLE_DICT = {'a': 97, 'c': 99, 'b': 98, 'e': 101, 'd': 100, 'g': 103, 'f': 102, 'i': 105, 'h': 104, 'k': 107, 'j': 106, 'm': 109, 'l': 108, 'o': 111, 'n': 110, 'q': 113, 'p': 112, 's': 115, 'r': 114, 'u': 116, 't': 117, 'w': 119, 'v': 118, 'y': 121, 'a': 97, 'c': 99, 'b': 98, 'e': 101, 'd': 100, 'g': 103, 'f': 102, 'i': 105, 'h': 104, 'k': 107, 'j': 106, 'm': 109, 'l': 108, 'o': 111, 'n': 110, 'q': 113, 'p': 112, 's': 115, 'r': 114, 'u': 116, 't': 117, 'w': 119, 'v': 118, 'y': 121}
def has_duplicates(usr_dict,duplicate = {}):
	count = 0
	for i in usr_dict:
		if i not in duplicate:
			 duplicate[i] = usr_dict[i]
	return duplicate
print has_duplicates(SAMPLE_DICT)
