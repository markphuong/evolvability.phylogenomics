import os
import sys

myref = open('conus.baits.2017.final.sliced.fa', 'r')

mymap = open('mymap', 'w')

out = open('conus.baits.2017.final.renamed.fa', 'w')

counter = 0

for line in myref:
	if ">" in line:
		out.write('>seq' + str(counter) + '\n')
		out.write(next(myref))
		mymap.write('>seq' + str(counter) + '\t' + line.strip() + '\n')

		counter += 1




