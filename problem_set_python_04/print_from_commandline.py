#!/usr/bin/env python3

import sys

first_num = sys.argv[1] #get low range number from command line
last_num = sys.argv[2] #get high range number from command line

#convert range numbers to int
int_first_num = int(first_num)
int_last_num = int(last_num) + 1

#print all numbers in range
for num in range(int_first_num, int_last_num):
	print(num)
print('\n')

#print all numbers in range that are odd
for num in range(int_first_num, int_last_num):
	if num % 2 == 1:
		print(num)
	else:
		continue

