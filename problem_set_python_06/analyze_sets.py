#!/usr/bin/env python3

set_a = {3,14,15,9,26,5,35,9}
set_b = {60,22,14,0,9}

intersection = set_a & set_b
difference = set_a - set_b
union = set_a | set_b
symmetrical_diff = set_a ^ set_b

print('intersection: ',intersection)
print('difference: ',difference)
print('union: ',union)
print('symmetrical_diff: ',symmetrical_diff)
