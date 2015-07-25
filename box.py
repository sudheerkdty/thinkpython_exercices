# Program to print a Box with 2x2 squares as in figure
#	+---+---+
#	|   |   |
#	|   |   |
#	+---+---+
#	|   |   |
#	|   |   |
#	+---+---+
# And also extend it to draw similar Big box with 4x4 squares

a = '+'
b = '-'
c = '|'
d = ' '

def two(a): 
	print a,a,

def four(a):
	two(a),two(a),

def block(a,b):#To generate block of symbols say +---
	print a,
	four(b),

def line(a,b): #To generate a line of symbols
	block(a,b)
	block(a,b)
	print a

def sbox():
	line(a,b)
	i=1
	while(i<4):
		line(c,d)
		i = i+1

def box():
	sbox()
	sbox()
	line(a,b)

print ("Box with 2x2 Squares")

box() 
def bline(a,b):
	i=0
	while(i<4):
		block(a,b)
		i = i+1
	print a

def fig():
	bline(a,b)
	i=1
	while(i<4):
		bline(c,d)
		i = i+1

def bbox():
	i=1
	while(i<5):
		fig()
		i = i+1
	bline(a,b)

print ("\n\nBox with 4x4 Squares")
bbox() ##Print a box with 4x4 Squares
