from swampy.TurtleWorld import *
world = TurtleWorld()
t = Turtle()
#print bob

def square(bob,length):
	for i in range(4):
		fd(bob, length)
		lt(bob)
		

length = 100

square(t, length)
 
wait_for_user()

