#!/usr/bin/env python3

import math

#create list full of nums and empty list
list = [101, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]
even_list = []
odd_list = []
sum_even_list = int(0)
sum_odd_list = int(0)

#sort elements of list
sorted_list = sorted(list)
print('sorted list is: ', sorted_list)

#iterate through each item in list, if even then store item in new list
for num in sorted_list:
	if num % 2 == 0:
		even_list.append(num)
	else:
		odd_list.append(num)

#sum even numbers
for num in even_list:
	sum_even_list = sum_even_list + num

#sum odd numbers
for num in odd_list:
	sum_odd_list = sum_odd_list + num

#print evens and odds
print('Sum of even numbers: ', sum_even_list)
print('Sum of odds: ', sum_odd_list)
