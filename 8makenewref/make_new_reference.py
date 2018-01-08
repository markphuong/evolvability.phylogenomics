import os
import sys
from collections import defaultdict

mybed = open('mynewbed', 'r') 

slicedict = defaultdict(list)

for line in mybed:

	info = line.strip().split('\t')
	print info
	if len(info[0].split('|')) > 7:
		continue

	elif info[0] in slicedict:
		slicedict[info[0]].append([int(info[1]), int(info[2])])
	else:
		slicedict[info[0]] = [ [int(info[1]), int(info[2])] ] 


myconus = open('conus.baits.2017.final' , 'r')

out = open('conus.baits.2017.final.sliced.fa', 'w')

for line in myconus:
	if ">" in line:
		name = line.strip()[1:]
		seq = next(myconus).strip()
		if name in slicedict:
			counter = 0


			for coords in sorted(slicedict[name]):
				out.write('>' + name + '|new_ref_locus' + str(counter) + '\n')
				out.write(seq[coords[0]:coords[1]] + '\n')
				counter += 1


		else:
			out.write('>' + name + '|new_ref_locus_not_cut_again' + '\n')
			out.write(seq + '\n')			

































