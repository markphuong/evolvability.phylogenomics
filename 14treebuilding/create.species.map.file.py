import os
import sys

mymap = open('species.map.file.v1', 'r')

mydict = dict()

out = open('species.map.file.v2', 'w')

for line in mymap:

	info = line.strip().split('\t')

	if info[1] in mydict.keys():
		mydict[info[1]] += 1
		info[1] = info[1] + str(mydict[info[1]])
		out.write('\t'.join(info) + '\n')
		
	else:
		mydict[info[1]] = 1
		out.write(line)