#!/usr/vin/env python3

set_line = {}

with open("alpaca_all_genes.tsv", "r") as all_genes_obj:
	for line in all_genes_obj:
		line = line.rstrip()
		set_line.add(line)
		print(set_line)
