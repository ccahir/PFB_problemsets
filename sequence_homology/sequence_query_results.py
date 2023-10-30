#!usr/bin/env python3

import sys
import os

input_dir = sys.argv[1] #input the directory with files in it

#initialize dictionary for final values
file_dict = {}

#iterate through files in directory inputted by command line - need absolute path
for file in os.listdir(input_dir):
  #add each file to dictionary with file name as key and id, alen, eval as dictionary in value
	file_dict[file] = {'id':'', 'alen':'', 'eval':''}
	#iterate through every file and open to read
	with open(f'{input_dir}/{file}', "r") as file_obj:
		for line in file_obj:
			line = line.rstrip() #remove lines

			#if the line doesn't start with a #, split on tabs
			if not line.startswit("#"):
				tab_list = line.split('\t')
				#extract id, alen, and eval to dictionary 
				file_dict[file]['id'] = tab_list[2]
				file_dict[file]['alen'] = tab_list[3]
				file_dict[file]['eval'] = tab_list[-2]
				break

#print(header for table
print(f"Matrix" \t "id" \t "alen" \t "eval")

#iterate throug each matrix and print the values of its dictionary tab sep
for matrix in file_dict:
	print(f"{matrix[0:-4]} \t {file_dict[matrix]['id']} \t {file_dict[matrix]['alen']} \t {file_dict[matrix]['eval']}")
