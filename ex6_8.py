a = int(raw_input("Enter a:"))
b = int(raw_input("Enter b:"))
rem = a % b
while rem ! = 0 :
    a = b
    b = rem
    rem = a % b
print "gcd: %d" %(b)
