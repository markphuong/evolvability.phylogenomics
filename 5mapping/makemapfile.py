import os
import sys
from collections import defaultdict
import multiprocessing
from os import listdir
from os.path import isfile, join




counter = 0
mapfilenum = 0

mymap = open('mapfile', 'r')



for line in mymap:
	if counter == 0:
		out = open('mapfile' + str(mapfilenum), 'w')
		out.write(line.strip() + '\n')
		counter += 1
		mapfilenum += 1
	elif counter > 0 and counter < 19:
		out.write(line.strip() + '\n')
		counter += 1
	else:
		out.write(line.strip() + '\n')
		out.close()
		counter = 0
