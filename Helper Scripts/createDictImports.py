import sys
import os
import pickle
import re

infile = sys.argv[1]
outputfile = sys.argv[2]
outfile = open(outputfile, 'w')

with open(infile, 'r') as imports:
	imports.readlines()

adversarial_imports_dict = {}
dll = ""

for line in imports:
	if ".dll" in line:
		dll = line
		if(dll not in adversarial_imports_dict):
			adversarial_imports_dict[dll] = []
	else:
		adversarial_imports_dict[dll] = line

for keys in adversarial_imports_dict:
	for value in adversarial_imports_dict[key]:
		outfile.write(key + ':' + value)

