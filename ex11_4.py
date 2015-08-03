#Program that returns list of keys that are mapped to entered value
SAMPLE_DICT = {'a': 97, 'c': 99, 'b': 98, 'e': 101, 'd': 100, 'g': 103, 'f': 102, 'i': 105, 'h': 104, 'k': 107, 'j': 106, 'm': 109, 'l': 108, 'o': 111, 'n': 110, 'q': 113, 'p': 112, 's': 115, 'r': 114, 'u': 116, 't': 117, 'w': 119, 'v': 118, 'y': 121, 'x': 120, 'z': 122}
def reverse_lookup(d,v,lis = []):
	for k in d:
		if d[k] == v:
			lis.append(k)
	return lis
	raise ValueError

print reverse_lookup(SAMPLE_DICT,116)
