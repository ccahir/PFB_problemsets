#!/usr/bin/env python3
 
import math

#extract nucleotides 100 (index 99) to 200 (index 199) 
sequence = input("Please enter a sequence: ")
sub_sequence = sequence[99:200]

print(f'\nnucleotides 100 to 200 are: {sub_sequence}\n')

#count number of capital and lowercase gs in nucleotides 100 to 200
Gs_in_sub_sequence = sub_sequence.count('G')
gs_in_sub_sequence = sub_sequence.count('g')

total_gs_sub_sequence = int(Gs_in_sub_sequence) + int(gs_in_sub_sequence)

print(f'\nnumber of Gs in nucleotides 100 to 200 are: {total_gs_sub_sequence}\n')
