import os
import sys

mydb = open('pbdb_data.conidae.txt', 'r')

out=open('pyrate.input.v1', 'w')

mygenera = []

for line in mydb:
	if 'record_type' in line:
		continue
	else:
		info = line.strip().split('\t')
		if 'species' in info[10]:
			genus = info[9].split(' ')[0]
			if '(' in info[9]:
				species = info[9].split(' ')[2]
			else:
				species = info[9].split(' ')[1]

			out.write('\t'.join([genus, species, 'NA', info[-2], info[-3]]) + '\n')  
			mygenera.append(genus)
		else:
			continue


		
print set(mygenera)	