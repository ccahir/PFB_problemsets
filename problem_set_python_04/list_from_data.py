#!/usr/bin/env python3

list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
count = 1

for sequence in list:
	print(count, '\t', len(sequence), '\t', sequence)
	count += 1
