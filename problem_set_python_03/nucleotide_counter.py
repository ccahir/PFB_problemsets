#!/usr/bin/env python3

import math

sequence = input("Please enter a sequence: ")

upper_sequence = sequence.upper()
number_of_As = upper_sequence.count('A')
number_of_Ts = upper_sequence.count('T')
number_of_Gs = upper_sequence.count('G')
number_of_Cs = upper_sequence.count('C')

print(f'A={number_of_As}, T={number_of_Ts}, G={number_of_Gs}, C={number_of_Cs}')
