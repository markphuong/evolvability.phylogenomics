import os
import sys


myfile = open('pyrate.input.v2', 'r')


out = open('pyrate.input.v3', 'w')

conuslist = [ 'Conasprelloides', 'Purpuriconus', 'Lithoconus']

for line in myfile:
	info = line.strip().split('\t')

	if info[0] in conuslist:
		info[0] = 'Conus'
		out.write('\t'.join(info) + '\n')

	elif 'Parviconus' == info[0]:
		info[0] = 'Conasprella'
		out.write('\t'.join(info) + '\n')
	elif 'Conospirus' == info[0]:
		info[0] = 'Conilithes'
		out.write('\t'.join(info) + '\n')
	else:
		out.write(line)