import os
import sys
from collections import defaultdict

mydict = defaultdict(dict)

myfile = open('conus.samples.v9.txt', 'r')

out = open('my.r.groupings', 'w')

myexclude = open('conus.excludethese.298', 'r')

excludelist  = []

for line in myexclude:
        excludelist.append(line.strip().split(' ')[0])


for line in myfile:
    if "gelsize" in line:
        continue
    else:
        info = line.strip().split('\t')
        if info[-10] == 'Conus':
            mykey = info[-8]
	    if info[-8] == 'Conasprella':
		mykey = info[8] + '.2'
        else:
            mykey = info[-10]
	if info[-1] in excludelist:
		continue

    if mykey in mydict:
        mydict[mykey].append(info[-1])
    else:
        mydict[mykey] = [info[-1]]

for thing in mydict:
	if len(mydict[thing]) == 1:
		continue

	out.write(thing + '=c(')

	for species in mydict[thing]:
		out.write("\"")
		out.write(species)
		out.write("\",")
	out.write(")," + '\n')
