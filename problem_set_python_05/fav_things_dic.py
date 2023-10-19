#!/usr/bin/env python3

import sys

user_fav_key = sys.argv[1] #get key from command line
user_value = sys.argv[2] #get value from command line

my_fav_things = {'book':'Pride and Prejudice', 'song':'I will follow you into the dark', 'tree':'tulip', 'organism':'S. aureus'}
fav_book = 'book'
fav_thing = 'organism'

print(my_fav_things['book']) #print favorite book
print(my_fav_things[fav_book]) #print favorite book using variable as key
print(my_fav_things['tree']) #print favorite tree
print(my_fav_things[fav_thing]) #print favorite organism using variable
print('\n')

#print out all key value pairs from dictionary
for key in my_fav_things:
	print(key, ':', my_fav_things[key])
print('\n')

#print value from user inputted key
#print(my_fav_things[user_key])
#print('\n')

#print all keys
for key in my_fav_things:
	print(key)
print('\n')

#change value of favorite organism
my_fav_things['organism'] = 'frog'
print(my_fav_things['organism'])
print('\n')

#get fav thing from command line and new value for key, change value with user inputted value
my_fav_things[user_fav_key] = 'mini starburst'
print(user_fav_key, ':', my_fav_things[user_fav_key])
my_fav_things[user_fav_key] = user_value
print(user_fav_key, ':', my_fav_things[user_fav_key])
