#!/usr/bin/env python3
import math
import sys

#get first command line parameter
input_number = float(sys.argv[1])

#test to see if number is positive of negative
if input_number > 0:
	print("positive")
	if input_number < 50:
		if input_number % 2 == 0:
			print("it is an even number that is smaller than 50")
	elif input_number > 50:
		if input_number % 3 == 0:
			print("it is larger tan 50 and divisible by 3")
elif input_number == 0:
	print("number is zero")
else:
	print("negative")
