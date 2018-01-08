import os
import sys

keydict = dict()

speciesfile = open('sampleIDs.txt', 'r')
counter = 0
for line in speciesfile:
	info = line.strip().split('\t')
	myID = info[1]
	counter +=1
	if 'OTU' in line:
		continue

	elif "_" in info[0]:
		#print line
		info = line.strip().split('\t')[0].split('_')
		if 'loyaltiensis' in line:
			keydict[myID] = [info[-1],line.strip()]
		#	print info[-1]
		elif 'white' in line:
			keydict[myID] = ['whiterolani',line.strip()]
		#	print 'whatrolani'				
		elif 'cf' in line:
			keydict[myID] = [info[1], line.strip()]
		#	print info[1]
		elif 'n.sp.' in line:
			info = line.strip().split('\t')
			keydict[myID] = [info[0], line.strip()]
		#	print info[-1]
		else:
			keydict[myID] = [info[0], line.strip()]
		#	print info[0]

	elif '.' in info[0]:
		#print line
		info = line.strip().split('\t')[0].split('.')
		keydict[myID] = [info[0], line.strip()]
		#print info[0]
	else:
		info = line.strip().split('\t')
		keydict[myID] = [info[0], line.strip()]

print keydict.keys()
#############

specieslist = []

for key in keydict:
	specieslist.append(keydict[key][0])

##################

helena = open('Species_sequenced.txt', 'r')

helenaspecies = []

for line in helena:
	
	if 'Species' in line or 'Conasprella' in line or 'caracteristics' in line or 'morelletti' in line or 'nanus' in line:
		continue
	elif 'Cs' in line:
		species = line.strip().split('_')[1]
		
		if species in keydict.keys():
			continue
		else:
			helenaspecies.append(species)
	else:
		species = line.strip()
		if species in specieslist:
			continue
		else:
			helenaspecies.append(species)
###########

classdict = dict()
myclass = open('speciesclassification.txt', 'r')

for line in myclass:
	info = line.strip().split('\t')
	classdict[info[0]] = line.strip()

###############

out = open('finalspecieslist.txt', 'w')
out.write('\t'.join(['species', 'sampleID', 'species', 'manologenus', 'moleculargenus', 'subgenus']) + '\n')
for thing in keydict.keys():

	if keydict[thing][0] in classdict:
		out.write(keydict[thing][1] + '\t' + classdict[keydict[thing][0]] + '\n')
	else:
		out.write(keydict[thing][1] + '\t' + keydict[thing][0] + '\n')

for thing in helenaspecies:
	if thing in classdict:
		out.write(thing + '\t' + 'helena' + '\t' + classdict[thing] + '\n')

	else:
		out.write(thing + '\t' + 'helena' + '\n')

















