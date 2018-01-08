from ete3 import Tree
import os
import sys
from collections import defaultdict
from numpy import mean

mytree = open('raxml.298.pruned.tre', 'r')

for line in mytree:
	t = Tree(line.strip(), format = 1)

mycalibs = open('calibrations.tab.txt', 'r')

for line in mycalibs:
	info = line.strip().split('\t')
	print info
	sp1 = info[0]
	sp2 = info[1]
	thetime = info[2]

	tempnode = t.get_common_ancestor(sp1, sp2)
	print sp1, sp2, tempnode
	tempnode.add_features(calibration = ">" + thetime)

out = open('conus.tree.calibrationsadded.tre', 'w')

out.write("365 7\n")
myoutput = t.write(format=9,features=["calibration"]).replace('[&&NHX:calibration=','').replace(']','')
out.write(myoutput + '\n')
out.write('//end of file')

#print t.write(format=9,features=["calibration"], outfile = "conus.tree.calibrationsadded.tre")

#node1 = t.get_common_ancestor("arcuata", "centurio")
#node1.add_features(calibration = ">0.1")







#ancestor = t.get_common_ancestor("mappa", "archon")



#print ancestor

#ancestor.add_features(calibration="what")

#print t.write(format=9,features=["calibration"])
