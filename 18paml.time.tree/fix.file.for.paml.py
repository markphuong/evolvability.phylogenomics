import os
import sys


droplist = []
mydata = open('conus.samples.v9.txt', 'r')

for line in mydata:
        if "gelsize" in line:
                continue
        else:
                info = line.strip().split('\t')
                try:
                        int(info[-1][-1])
                        droplist.append(info[-1])
                except:
                        continue

droplist.append("nigropunctatus")
droplist.append("excelsus")
droplist.append("gradatus")
droplist.append("lorenzianus")
droplist.append("Outgroup")

myfasta = open("conus_phylogeny_headed_298.nexus", 'r')

out = open('conus.alignment.paml', 'w')

for line in myfasta:
	if ";" in line:
		continue
	elif line.strip().split(' ')[0] in droplist:
		continue
	else:
		out.write(line.replace(' ','  '))
