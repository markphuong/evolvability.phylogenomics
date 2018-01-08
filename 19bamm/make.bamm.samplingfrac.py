import os
import sys


##################################### count total num per genus

myworms = open('all.conidae.worms.12.2.2017', 'r')

wormsdict = dict()

for line in myworms:
	genus = line.strip().split(' ')[0]
	if genus in wormsdict:
		wormsdict[genus] += 1
	else:
		wormsdict[genus] =1 

genusdict = dict()

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
			genusdict[info[-1]] = info[-10]
                        continue

droplist.append("nigropunctatus")
droplist.append("excelsus")
droplist.append("gradatus")
droplist.append("lorenzianus")
droplist.append("Outgroup")

myfasta = open("conus_phylogeny_headed_298.nexus", 'r')

#print genusdict

out = open('bamm.298.samplingfrac', 'w')

#out.write("              304        107011" + '\n')

keeplist = []

counterdict = dict()

for line in myfasta:
	if ";" in line or "NEXUS" in line or 'matrix' in line:
		continue
	elif line.strip().split(' ')[0] in droplist:
		continue
	else:
		myspecies = line.strip().split(' ')[0]
		keeplist.append(myspecies)
		if genusdict[myspecies] in counterdict.keys():
			counterdict[genusdict[myspecies]] += 1
		else:
                        counterdict[genusdict[myspecies]] = 1


for species in keeplist:
	out.write('\t'.join([species, genusdict[species], str(float(counterdict[genusdict[species]])/wormsdict[genusdict[species]]) ] ) + '\n' )

print keeplist

print len(keeplist)
print counterdict
print wormsdict
