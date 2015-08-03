import timeit
known = {0:0,1:1}
def fibonacci_dict(n):
	if n in known:
		return known[n]
	res = fibonacci_dict(n-1) + fibonacci_dict(n-2)
	known[n] = res
	return res
def fibonacci_old(n):
	if n==0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci_old(n-1) + fibonacci_old(n-2)
time1=time2 =0.0
start1 = timeit.timeit()
val1 = fibonacci_dict(30)
end1 = timeit.timeit()
time1 = end1 - start1

start2 = timeit.timeit()
val2 = fibonacci_old(30)
end2 = timeit.timeit()
time2 = end2 - start2

print "Value for fibonacci_dict(30) and fibonacci_old(30) are \n%d\t%d\nTime for fibonacci_dict(30) and fibonacci_old(30) are \n%d\t%d\n"%(val1,val2,time1,time2)
