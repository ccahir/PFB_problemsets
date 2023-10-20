#!/usr/bin/env python3

import re

#open fasta file
with open("Python_07.fasta", "r") as fasta_file:

	#iterate through each line of fasta file
	for line in fasta_file:
		line = line.rstrip()

		#save match as new variable from .search()
		match = re.search(r"^>(\S+)\s(.+)", line)
		#if match is True, print. if match is False, continue
		if match:
			#take whole fasta header and store in variable
			print(match.group(0))
			print(f'id:{match.group(1)} desc:{match.group(2)}')
