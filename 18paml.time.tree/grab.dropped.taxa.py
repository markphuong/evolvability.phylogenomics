import os
import sys

out = open('mydroppedtaxa', 'w')

droplist = []

mytaxanum = []

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
			mytaxanum.append(info[-1])
			continue

for thing in droplist:
	out.write("\"" + thing +  "\"," + '\n')

out.write('\"nigropunctatus\",' + '\n')
out.write('\"excelsus\"' + '\n')
out.write('\"gradatus\"' + '\n')
out.write('\"lorenzianus\"' + '\n')

out.write('\"Outgroup\"' + '\n')

print mytaxanum
print len(mytaxanum)
