import os
import sys
from collections import defaultdict
from Bio.Seq import reverse_complement


thedir = [f for f in os.listdir('.') if os.path.isfile(f)]

myconus = open("conus.baits.2017.final.renamed.fa", 'r')

for line in myconus:

	out = open(line.strip()[1:] + '.conusfasta', 'a')


        out.write(line)
        out.write(next(myconus))

        out.close()



for thing in thedir:
	if 'loci_v2.fa' in thing:
		

		ID = thing.split('_')[0]


		myfasta = open(thing, 'r')

		alreadyseen = []

		for line in myfasta:
			if ">" in line:
				info = line.strip().split('|')

				

				out = open(info[-1] + '.exonfasta', 'a')


				out.write(line)
				out.write(next(myfasta))

				out.close()

		myfasta.close()



thedir = [f for f in os.listdir('.') if os.path.isfile(f)]


for thing in thedir:
	if 'exonfasta' in thing:
		cmd = '/home/phuong/mafft/bin/mafft --adjustdirection --addfragments ' + thing + ' ' + thing[:-9] +'conusfasta > ' + thing + '.aligned'
		os.system(cmd)





















