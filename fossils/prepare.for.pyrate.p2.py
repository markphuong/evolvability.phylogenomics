import os
import sys
from collections import defaultdict

myfile = open('pyrate.input.v1', 'r')

out = open('pyrate.input.v2', 'w')


keptgenera = ['Conilithes', 'Californiconus', 'Conasprella', 'Conasprelloides', 'Purpuriconus', 'Profundiconus', 'Conus', 'Lithoconus', 'Parviconus', 'Conospirus']

genusdict = defaultdict(list)

for line in myfile:
	info = line.strip().split('\t')

	if info[0] in keptgenera:
		out.write(line)

		if info[0] in genusdict:
			genusdict[info[0]].append(info[1])
		else:
			genusdict[info[0]] = [info[1]]
	else:
		continue


for genus in genusdict:
	myspecieslist = list(set(genusdict[genus]))

	for species in myspecieslist:
		for item in genusdict:
			if genus == item:
				continue
			else:
				if species in genusdict[item]:
					print species

