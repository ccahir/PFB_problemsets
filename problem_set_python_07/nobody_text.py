#!/usr/bin/env python3

import re
import sys

fav_name = sys.argv[1] #get favorite name from command line

#open Python 07 nobody txt
nobody_file_obj = open("Python_07_nobody.txt", "r")
contents = nobody_file_obj.read() #add contents of file to string
nobody_file_obj.close() #close file

#iterate through the nobody file contents
for nobody in re.finditer(r"(Nobody)", contents):

	whole_nobody = nobody.group(0)
	nobody_start = nobody.start(1) + 1
	nobody_end = nobody.end(1)
		
	print(whole_nobody, nobody_start, nobody_end, sep='\t')

#open new file and substitute Nobody with favorite name
#fav_name_obj = open(fav_name.txt, "w")
outfile = fav_name + '.txt' #convert variable to hold name
with open(outfile, "w") as fav_name_write:

	for line in contents:
		fav_name_contents = re.sub(r"(Nobody)", fav_name, contents)
	
	fav_name_write.write(fav_name_contents)

#close favorite name file
#fav_name_obj.close()
