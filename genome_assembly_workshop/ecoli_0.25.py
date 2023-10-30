#!/usr/bin/env python3

import sys
import Bio.Seq
from Bio import SeqIO

#help message
if len(sys.argv) < 2:
	print(f'Usage: {sys.argv[0]} <fasta file>')
	exit(1)

fasta_file = sys.argv[1] #import fasta file name from command line

#check for fasta file
if not fasta_file.endswith(('.fa','.fasta')):
	print("Input file needs to end with .fa or .fasta")

#initialize variables
sequence_dict = {}
list_of_keys = []
total_contig_len = 0

#read in fasta file and convert to dictionary with seq id as key and sequence as value
for seq_record in SeqIO.parse(fasta_file, "fasta"):
	sequence_dict[seq_record.id] = str(seq_record.seq)

#report the number of contigs in the file
number_contigs = len(sequence_dict)
print(number_contigs)

#use sorted function with lambda to sort dictionary by length of values into list of keys
list_of_keys = sorted(sequence_dict, key=lambda k: len(sequence_dict[k]), reverse=True)
min_contig_key = list_of_keys[-1]
len_min_contig = len(sequence_dict[min_contig_key])
max_contig_key = list_of_keys[0]
len_max_contig = len(sequence_dict[max_contig_key])

#print min contig ID and lengt and max contig ID and length
print(f'{min_contig_key}: {len_min_contig}')
print(f'{max_contig_key}: {len_max_contig}')

#calculate total contig length 
for key in list_of_keys:
	len_contig = len(sequence_dict[key])
	total_contig_len = total_contig_len + len_contig
print(f'total contig length: {total_contig_len}')

#calculate the 50% point of total contig length
fifty_percent = total_contig_len / 2

#initalize some new variables
count = 0
list_of_lens = []

#interate through list of keys to add length in descending order to new list of contig lengths
for key in list_of_keys:
	list_of_lens.append(len(sequence_dict[key]))

#iterate through list of contig lengths to add until hits 50% point of total contig length
for item in list_of_lens:
	if count < fifty_percent:
		count = count+item
	else:
		n50_index = list_of_lens.index(item) - 1
		n50_size = list_of_lens[list_of_lens.index(item) - 1]
		break
print(f'N50 size = {n50_size}')

#calculate the L50 size
l50_size = n50_index + 1
print(f'L50 size = {l50_size}')
