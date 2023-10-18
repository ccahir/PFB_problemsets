#!/usr/bin/env python3

import math

sequence = input("Please enter a sequence: ")

#reverse original sequence
reverse_sequence = sequence[::-1]

#make reverse sequence lowercase
lower_reverse = reverse_sequence.lower()

#complement reverse lowercase sequence converting to uppercase sequence
reverse_complement = lower_reverse.replace('a','T').replace('t','A').replace('g','C').replace('c','G')

print(f'Original Sequence {5:3}\' {sequence} 3\'')
print(f'Reverse {3:13}\' {reverse_sequence} 5\'')
print(f'Reverse Complement {5:2}\' {reverse_complement} 3\'')
