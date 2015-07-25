import math
num = raw_input('enter a number:')
a = raw_input('enter a :')
def sqrt(a,x):
	y = 0.0
	y = ((x + (a / x)) / 2)
	return y


newtons_root = normal_root = difference = 0.0
newtons_root = sqrt(float(a),float(num))
normal_root = math.sqrt(float(num))
difference = normal_root -newtons_root 
print "newtons_root normal_root difference"
print "\n%f\t%f\t%f" %(newtons_root,normal_root,difference)
