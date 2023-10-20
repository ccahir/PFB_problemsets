#!/usr/bin/env python3

sequence = 'GAACTCC'
unique = set(sequence)

#print sequence
print(sequence)

#determine unique caracters in sequence
print('unique characters in sequence: ',unique)

#create new empty dictionary
nt_comp = {}

#iterate through each unique nucleotide
for nt in unique:

	#count the number of this unique nt in sequence
	count = sequence.count(nt)

	#add count to dict
	nt_comp[nt] = count

print('nt composition: ', nt_comp)

#iterate through dict to calculate number of GCs and number of ATs
gc_count = 0
ac_count = 0

for nt in nt_comp:
	if nt == 'G':
		gc_count = gc_count + int(nt_comp[nt])
	elif nt == 'C':
		gc_count = gc_count + int(nt_comp[nt])
	elif nt == 'A':
		ac_count = ac_count + int(nt_comp[nt])
	elif nt == 'T':
		ac_count = ac_count + int(nt_comp[nt])
	else:
		continue

#calculate GC content
gc_content = '{:.2f}'.format(gc_count / (gc_count+ac_count))

print(gc_content)

