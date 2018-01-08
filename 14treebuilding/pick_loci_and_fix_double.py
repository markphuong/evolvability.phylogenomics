import os
import sys
from collections import defaultdict
import argparse

from os.path import isfile, join



###### create consensus between exons in multiple sequences

def create_consensus(seq1, seq2):
        """Sequences must be strings, have the same length, and be aligned"""
        out_seq = ""

	counter = 0

        for i, nucleotide in enumerate(seq1):
                couple = [nucleotide, seq2[i]]
                if couple[0] == "-" or couple[0] == "n" or couple[0] == "N":
                        out_seq += couple[1]
                elif couple[1] == "-" or couple[1] == "n" or couple[1] == "N":
                        out_seq += couple[0]
                elif couple[0] == couple[1]:
                        out_seq += couple[0]
                elif not couple[0] == couple[1]:
                        out_seq += couple[0]
			counter += 1
        return [out_seq, counter]


############### map sample to a species name

mymap = open('species.map.file.v2', 'r')

speciesdict = dict()

for line in mymap:
        info = line.strip().split('\t')

        speciesdict[info[0]] = info[1]

######## open species to exclude




excludelist =[]

with open('excludethese') as rfile:
	for line in rfile:
		line = line.strip()
		excludelist.append(line)




thedir = [f for f in os.listdir('/pylon2/bi4s86p/phuong/evolvability/13fasta_and_align/aligned/') if isfile(join('/pylon2/bi4s86p/phuong/evolvability/13fasta_and_align/aligned/', f))]




counter = 0
for thing in thedir:
	if '.aligned' in thing:

		cmd = 'cp /pylon2/bi4s86p/phuong/evolvability/13fasta_and_align/aligned/' + thing + ' ./'
		os.system(cmd)
		cmd = "python makesomethingNotInterleaved.py " + thing + " " + thing + ".NI"
		os.system(cmd)

		myfasta = open(thing + '.NI', 'r')

		fastadict = defaultdict()




		for line in myfasta:
			if ">" in line:
				seq = next(myfasta).strip()
				if ">_R_" in line:
					ID = line.strip().split('|')[0][4:]
				else:
					ID = line.strip().split('|')[0][1:]

				if ID in excludelist:
					continue
				elif 'seq' in ID:
					continue
				elif ID in fastadict:
					fastadict[ID].append([line, seq])

				else:
					fastadict[ID] = [[line, seq]]					
		
		if len(fastadict) >= int(sys.argv[1]):
			keepdict = dict()

			for key in fastadict:
				if len(fastadict[key]) == 1:
					keepdict[">" + speciesdict[key] + '\n'] = fastadict[key][0][1] + '\n'
				else:
					mylist = fastadict[key]


					########## store sequences into a new dictionary, ordered by the first coordinate of the blast query on the lottia protein so you analyze sequences in order
					tempdict = dict()
					counter =0
					for item in mylist:
						tempdict[int(counter)] = item[1]
						counter += 1

					mytempkeys = sorted(tempdict) # holds the keys, which are the start of the blast query on the lottia protein ID taken from the fasta header

					##################### 
					n = 2
					different = 0

					consensus = create_consensus(tempdict[mytempkeys[0]], tempdict[mytempkeys[1]])

					consensus_seq = consensus[0]

					different = different + consensus[1]

					while n < len(mylist):

						consensus = create_consensus(consensus_seq, tempdict[mytempkeys[n]])

						consensus_seq = consensus[0]
						different = different + consensus[1]

						n += 1


					if different > 5:
						print thing
						print key
						continue
					else:
						keepdict[">" + speciesdict[key] + '\n'] = consensus_seq + '\n'
					
			if len(keepdict) >= int(sys.argv[1]):	
				out = open(thing + '_analyze.fasta', 'w')
				for item in keepdict:
					out.write(item)
					out.write(keepdict[item])

			else:
				continue

			


		else:
			continue	
	else:
		continue







