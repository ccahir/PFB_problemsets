#!/usr/bin/env python3

import math

sequence = input("Please enter a sequence: ")

upper_sequence = sequence.replace('T', 'U') #convert all Ts to Us
lower_sequence = upper_sequence.replace ('t', 'u') #convert all ts to us

print(f'\n{lower_sequence}')
