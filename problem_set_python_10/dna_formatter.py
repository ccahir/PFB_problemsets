#!/usr/bin/env python3

import sys
import Bio.Seq
from Bio import SeqIO

fasta_file = sys.argv[1] #get fasta file name from command line
line_length = int(sys.argv[2]) #get max length of each line from command line, convert to int

#create function that formats sequences of DNA from a fasta file to user defined lengthand writes newly formatted sequences to new fasta file
def dna_formatter(fasta_file, width):

	count = 0
	sequence_dict = {}
	formated_string = ''
	formated_string_dict = {}

	#read in fasta file and convert to dictionary with seq id as key and seq as value
	for seq_record in SeqIO.parse(fasta_file, "fasta"): 
		sequence_dict[seq_record.id] = seq_record.seq

	#open new fasta file to write to 
	with open("formated_fasta.fasta", "w") as handle:
		
		#iterate through each sequence in dictionary and remove all new lines
		for seq_id in sequence_dict:
			handle.write(f'>{seq_id}\n') #add sequence id to new fasta
			sequence = str(sequence_dict[seq_id])
			no_n_sequence = sequence.replace("\n", "") #remove all new lines in sequences
 
			#iterate through each nt in sequence and format into max length of line
			for nt in no_n_sequence:
				if count < width:
					formated_string = formated_string + nt
					count += 1
				else:
					formated_string = formated_string + "\n"
					count = 0
			handle.write(f'{formated_string}\n') #add formated string to new fasta
			print(f'{formated_string}\n')
			
	return "formated_fasta.fasta" 

dna_formatter(fasta_file, line_length)
