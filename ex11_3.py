#Program accepts a dict and print it in sorted order of keys
SAMPLE_DICT = {'a': 97, 'c': 99, 'b': 98, 'e': 101, 'd': 100, 'g': 103, 'f': 102, 'i': 105, 'h': 104, 'k': 107, 'j': 106, 'm': 109, 'l': 108, 'o': 111, 'n': 110, 'q': 113, 'p': 112, 's': 115, 'r': 114, 'u': 117, 't': 116, 'w': 119, 'v': 118, 'y': 121, 'x': 120, 'z': 122}
def print_hist(h):
	for c in sorted(h.keys()): #b is a list with keys of dict h & sorts list b
		print c,h[c] #print keys and values of dict h 

print_hist(SAMPLE_DICT)
