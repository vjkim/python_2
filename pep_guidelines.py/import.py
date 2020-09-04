import os
import sys
# always import different things on seperate lines

from MyModule import foo, bar, foobar
# this is fine


def my_function(one, two,
				 three, four,
				 five, six):
	print("Hello world")
#There must be 2 lines before top level functions and def


def second_function():
	print("Second Function")


my_list = [1, 2, 
		   3, 4, 
		   5, 6] 
# Proper indentation
# Recommended to use four space characters

print("Hello")

x = 3*52+7
# No whitespace

check = True

if check is True:
	print("This is true.")


func_one()
func_two()
# Call different functions on different lines