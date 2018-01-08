#!/usr/bin/env python

import os
import sys
import argparse
import multiprocessing


def get_args():
	parser = argparse.ArgumentParser(description="run blastx")
	required = parser.add_argument_group("required arguments") 
	required.add_argument("--map", help="textfile with samples to run and what fasta file to match it to", required=True) #A map file with the sample ID and the fasta file it goes to

	return parser.parse_args()


def align(element):



	variables = dict(
	sampleID = element) #name your output


	commands = """
	cp /pylon5/bi4s86p/phuong/evolvability/2trim/{sampleID}.final1.fq ./
	cp /pylon5/bi4s86p/phuong/evolvability/2trim/{sampleID}.final2.fq ./
	cp /pylon5/bi4s86p/phuong/evolvability/2trim/{sampleID}.finalunpaired.fq ./
	/home/phuong/SPAdes-3.8.1-Linux/bin/spades.py -m 768 -1 {sampleID}.final1.fq -2 {sampleID}.final2.fq -s {sampleID}.finalunpaired.fq -o {sampleID}
	cp -r {sampleID}/ /pylon5/bi4s86p/phuong/evolvability/3assembly
	""".format(**variables)

	cmd_list = commands.split("\n")
	for cmd in cmd_list:
		os.system(cmd)

mylist = []

args = get_args() 


with open(args.map) as rfile:
	for line in rfile:
		line = line.strip()
		mylist.append(line)


pool = multiprocessing.Pool(3)
pool.map(align, mylist)







