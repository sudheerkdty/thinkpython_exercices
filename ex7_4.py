#Program to evalute Expressions using eval
import math
expr = raw_input("""Enter an expression: \n Like 5+3 or (2*(5+9)\nType Quit or quit() to exit\n >>>""")
while True:
	if expr == 'Quit':
		quit()
	else:
		print expr
		print eval(expr)
		expr = raw_input(">>>")
