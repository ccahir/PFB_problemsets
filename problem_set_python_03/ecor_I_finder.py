#!/usr/bin/env python3

import math

sequence = input('Please input a sequence: ')

ecorI_site = 'GAATTC'

start_nucleotide = int(sequence.find(ecorI_site)) + 1
end_nucleotide = start_nucleotide + 5

print(f'EcoRI startPos:{start_nucleotide}  endPos:{end_nucleotide}')
