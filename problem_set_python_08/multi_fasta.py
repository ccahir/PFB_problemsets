#!/usr/bin/env python3

import sys
import re

#initialize variables 
file = ''
fasta_dict = {}

#write exception for if user does not give file name or file does not exist
try:
	file = sys.argv[1]
	print("User provided file name:", file)
	
	#open file if exists
	multi_fasta = open(file, 'r')
	
	#iterate through each line of fasta file
	for line in multi_fasta:
		line = line.rstrip()
		
		#save match as new variable from .search()
		match = re.search(r"^>(\S+)\s(.+)", line)

		#if match is True, create variable with sequence name, initialize sequence string
		if match:
			seq_name = match.group(1)
			sequence = ''

		#if line does not match the header format, 
		else:
			nt_counter = {}
			sequence = sequence + line
			unique = set(sequence)

			#iterate through each nt of sequence
			for nt in unique:
				count = sequence.count(nt)
				#populate nt_counter dic with nt as key and count as value
				nt_counter[nt] = count
			
			#populate fasta dictionary with seq_name as key and nut_counter as value
			fasta_dict[seq_name] = nt_counter
	
	#iterate through each key(seq_name) of dictionary, print seq_name and count of each nt 
	for key in fasta_dict:
		print(f"{key}\t{fasta_dict[key]['A']}\t{fasta_dict[key]['T']}\t{fasta_dict[key]['G']}\t{fasta_dict[key]['C']}")

except IndexError:
	print("Please provide a file name.")

except IOError:
	print("Can't find file:", file)
