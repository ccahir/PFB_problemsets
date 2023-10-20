#!/usr/bin/env python3

#set up empty dict
genes = {}

#open sequence text file and compile into dictionary
with open("Python_06.seq.txt", "r") as seq_read:
	for line in seq_read:
		line = line.rstrip()
		gene_id, seq = line.split()
		genes[gene_id] = seq

#print(genes)

#reverse complement every value of dictionary, add to new dictionary
reverse_comp_genes = {}

#iterate through each key of genes dict
for key in genes:
	gene = genes[key]
	reverse = gene[::-1] #reverse gene sequence 
	lower_reverse = reverse.lower() #make gene sequence lowercase
	reverse_comp = lower_reverse.replace('a','T').replace('t','A').replace('g','C').replace('c','G') #reverse complement
	reverse_comp_genes[key] = reverse_comp
#print(reverse_comp_genes)

#print each output in FASTA format
	
