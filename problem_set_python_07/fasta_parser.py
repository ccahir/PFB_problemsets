#!/usr/bin/env python3

import re

fasta_dict = {} #initialize empty dictionary to store fastas
count = 0

#open fasta file
with open("Python_07.fasta", "r") as fasta_file:

	#iterate through each line of fasta file
	for line in fasta_file:
		line = line.rstrip()

		#save match as new variable from .search()
		match = re.search(r"^>(\S+)\s(.+)", line)
		
		#if match is True, increase count 
		if match:
		#take whole fasta header and store in variable
		#print(match.group(0))
		#print(f'id:{match.group(1)} desc:{match.group(2)}')
			count += 1
			key_name = 'seq'+str(count)
			sequence = ''
		
		else:
			sequence = sequence + line
			fasta_dict[key_name] = sequence

	print(fasta_dict)
