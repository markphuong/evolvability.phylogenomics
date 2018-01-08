import os
import sys


myfile = open('pyrate.input.v5', 'r')

out = open('pyrate.input.v6', 'w')

out.write('\t'.join(['Species', 'Status','min_age','max_age']) + '\n')

for line in myfile:
	info = line.strip().split('\t')

	out.write('\t'.join([info[0] + '_' + info[1], info[2], info[3], info[4]]) + '\n')