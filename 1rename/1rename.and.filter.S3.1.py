#!/usr/bin/env python

#this concatenates all read files into read1 and read2 files [if you get multiple read files per index from illumina]

import os
import sys
import argparse
import multiprocessing

#manip these variables

ID = '.gz' #An ID common to all fastq files

### the script

directory = '/pylon2/bi4s86p/phuong/evolvability/0data/gslserver.qb3.berkeley.edu/170701_100PE_HS4KA/Lane23568/Alfaro/S3'


def concat(element):
	
	newname = element.split('/')
	newname = newname[-1]
	oldfile = newname
	newname = newname.split('_')
	myfilename = newname[0] +'.' + newname[1] + '.' + newname[-2] + '.lane1.fq.gz'

	print oldfile
	print myfilename

	variables = dict(
	index = str(element),
	oldfile = str(oldfile),
	newfile = str(myfilename))




	commands = """
	echo "Processing {index}"
	cp {index} ./
	zcat {oldfile} | grep -A 3 '^@.* [^:]*:N:[^:]*:' | grep -v "^--$" | sed 's/ 1:N:0:.*/\\/1/g' | sed 's/ 2:N:0:.*/\\/2/g' | gzip > {newfile}
	cp {newfile} /pylon2/bi4s86p/phuong/evolvability/1rename
	""".format(**variables)

	cmd_list = commands.split("\n")
	for cmd in cmd_list:
		os.system(cmd)

mylist = []

for root, dirs, files in os.walk(directory):
	for filename in files:
		path = os.path.join(root, filename)
		if ID in filename:	
			mylist.append(path)
		else:
			continue

pool = multiprocessing.Pool(40)
pool.map(concat, mylist)


