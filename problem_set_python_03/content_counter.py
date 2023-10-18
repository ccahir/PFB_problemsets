#!/usr/bin/env python3

import math

dna_string = input("Please enter a sequence: ")

#calculate number of each nucleotide
upper_sequence = dna_string.upper()
number_of_As = upper_sequence.count('A')
number_of_Ts = upper_sequence.count('T')
number_of_Gs = upper_sequence.count('G')
number_of_Cs = upper_sequence.count('C')

#math calculations to find proportion of AT
number_of_ATs = int(number_of_As) + int(number_of_Ts)
number_of_total_bases = int(number_of_As) + int(number_of_Ts) + int(number_of_Gs) + int(number_of_Cs)
proportion_of_AT = number_of_ATs / number_of_total_bases

#math calculation to find proportion of GC
proportion_of_GC = 1 - proportion_of_AT
percent_GC = proportion_of_GC * 100

print(f'\nThe AT content of this DNA string is {proportion_of_AT}')
print(f'The GC content of this DNA string is {percent_GC}%')
