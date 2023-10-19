#!/usr/bin/env python3

dna_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
lengths = [len(dna) for dna in dna_list]

#make list of tuples
list_tuples = list(zip(lengths, dna_list))

print(list_tuples)
