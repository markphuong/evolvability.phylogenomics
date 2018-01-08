import os
import sys

from os import listdir
from os.path import isfile, join



#!/usr/bin/env python


import os
import sys
import argparse
import multiprocessing



def align(element):

	ID = element
	

# some names for input output files

	variables = dict(
	sample = ID,
	myseq = ID.split('.')[0],
	mypath = '/pylon2/bi4s86p/phuong/evolvability/14treebuilding/50nexus'
	) #name your output

	commands = """
	cp {mypath}/{sample} ./
	python fasta2Nexus.py {sample} {myseq}.nexus
	python nexus2phylip.py {myseq}.nexus {myseq}.phylip
	raxmlHPC-PTHREADS-AVX2 -s {myseq}.phylip -m GTRGAMMA -n {myseq} -T 5 -p 1234
	cp {myseq}.phylip /pylon2/bi4s86p/phuong/evolvability/16astral/50phylip
	cp RAxML*{myseq}* /pylon2/bi4s86p/phuong/evolvability/16astral/50raxml
	""".format(**variables)



	cmd_list = commands.split("\n")
	for cmd in cmd_list:
		os.system(cmd)

mypath = '/pylon2/bi4s86p/phuong/evolvability/14treebuilding/50nexus'
mylist = []
def main():



	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


	for thing in onlyfiles:
		mylist.append(thing)

	pool = multiprocessing.Pool(8)
	pool.map(align, mylist)#run the function with the arguments

if __name__ == "__main__": #run main over multiple processors
	main()







