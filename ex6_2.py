import math
def hypotenuse(a,b):
	sqa = a * a
	sqb = b * b
	sumsq = sqa + sqb
	result = math.sqrt(sumsq)
	return result

a = raw_input("Enter side a of right triangle\n")
b = raw_input("Enter side b of right triangle\n")
print "The hypotenuse of given right angled triangle is :"
s =hypotenuse(int(a),int(b))
print s
