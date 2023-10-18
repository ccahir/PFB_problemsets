#!/usr/bin/env python3

import math

sequence = input("Please enter a sequence: ")

upper_sequence = sequence.upper() #convert all characters to uppercase

converted_sequence = upper_sequence.replace('T', 'U') #convert all Ts to Us

print(f'\n{converted_sequence}')
