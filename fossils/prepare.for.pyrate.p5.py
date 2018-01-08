import os
import sys


myfile = open('pyrate.input.v4', 'r')

out = open('pyrate.input.v5', 'w')


for line in myfile:
	info = line.strip().split('\t')

	if info[1] == info[-1].split(' ')[-1]:
		info[2] = 'extant'
		out.write('\t'.join(info) + '\n')
	elif info[1] == 'largillierti':
		info[2] = 'extant'
		out.write('\t'.join(info) + '\n')	
	else:
		out.write(line)