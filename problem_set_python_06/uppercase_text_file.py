#!/usr/bin/env python3

#open new file to write uppercase text to
up_text_file = open("Python_06_uc.txt", "w")

#open file
with open("Python_06.txt", "r") as text_file_obj: 
	
	#iterate through each line of file, make uppercase, write to new file
	for line in text_file_obj:
		line = line.rstrip()
		up_line = line.upper()
		up_text_file.write(f'{up_line}\n')
		print(up_line)

