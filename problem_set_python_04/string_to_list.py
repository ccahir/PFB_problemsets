#!/usr/bin/env python3

taxa = 'sapiens, erectus, neanderthalensis'

print(taxa)
print(taxa[1])
print(type(taxa),'\n')

#split taxa by commas into individual words
species = taxa.split(',')
print(species)
print(species[1])
print(type(species),'\n')

#sort list alphabetically
alphabetical_species = sorted(species)
print(alphabetical_species)

#sort list by length of each string
length_species = sorted(species, key=len)
print(length_species)
