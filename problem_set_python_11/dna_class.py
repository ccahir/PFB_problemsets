#!/usr/bin/env python3

###Start of CLASS DNARecord###
class DNARecord(object):
	#define class attributes
	def __init__(self, sequence, gene_name, species_name): 
		self.sequence = sequence
		self.gene_name = gene_name
		self.species_name = species_name

	#add method to class that calculates and returns the length of the sequence
	def seq_len(self): 
		length = len(self.sequence)
		return length

	#add method tat calculates and returns the nucleotide composition
	def nuc_comp(self):
		nuc_comp_dict = {'A':0, 'T':0, 'G':0, 'C':0}
		a_count = self.sequence.count('A')
		nuc_comp_dict['A'] = a_count
		t_count = self.sequence.count('T')
		nuc_comp_dict['T'] = t_count
		g_count = self.sequence.count('G')
		nuc_comp_dict['G'] = g_count
		c_count = self.sequence.count('C')
		nuc_comp_dict['C'] = c_count
		return nuc_comp_dict

	#add method tat returns the GC content
	def gc_content(self):
		length = len(self.sequence)
		g_count = self.sequence.count('G')
		c_count = self.sequence.count('C')
		gc_count = g_count + c_count
		gc_cont = gc_count / length
		return gc_cont			
		
	#add method that returns the sequence record in FASTA format
	def fasta_formatter(self):	
		header = f'>{self.gene_name} | {self.species_name}'
		sequence = f'{self.sequence}'
		fasta_formatted = f'{header}\n{sequence}'
		return fasta_formatted
	
#add a DNARecord object
dna_rec_obj_1 = DNARecord('ACTGATCGTTACGTACGAGT', 'ABC1', 'Drosopila melanogaster')

#use object sequence, name, organism that retrieves and prints 
print('name:', dna_rec_obj_1.gene_name , ' ', 'seq:' , dna_rec_obj_1.sequence, ' ', 'species:' , dna_rec_obj_1.species_name, ' ', 'seq len:' , dna_rec_obj_1.seq_len(),' ', 'nuc comp:' , dna_rec_obj_1.nuc_comp(),' ', 'gc content:' , dna_rec_obj_1.gc_content())

print(dna_rec_obj_1.fasta_formatter())
