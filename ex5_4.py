a = int(raw_input('a='))
b = int(raw_input('b='))
c = int(raw_input('b='))
conditions = [a > (b + c), b > (a + c), c > (a + b)]
 
def triangle(a, b, c):
    for i in conditions:
        if i:
            print 'No'
            return
    else:
        print 'Yes'
triangle(a, b, c)
