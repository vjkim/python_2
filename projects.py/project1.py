'''
	Program: Magical Calculator
	Author: V Kim
	Copyright:2020

'''

import re

print("Our Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True


def performMath():
	global run
	global previous
	equation = ""

# If there has been a previous thing, use this.
	if previous == 0:
		equation = input("Enter equation:")
	else:
		equation = input(str(previous))

# If the user quits
	if equation == 'quit':
		print("Goodbye human!")
		run = False
	else:
		equation = re.sub('[a-zA-Z,.()""]',' ', equation)

	if previous == 0:
		previous = eval(equation)
	else:
		previous = eval(str(previous) + equation)

while run:
	performMath()
