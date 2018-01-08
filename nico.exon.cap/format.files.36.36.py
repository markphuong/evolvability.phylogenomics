import os
import sys


def checkoverlap(a, b):
        overlap = max(0, min(a[1], b[1]) - max(a[0], b[0]))
        length1 = len(range(a[0],a[1]+1))

        length2 = len(range(b[0],b[1]+1))

        ratio1 = float(overlap)/length1
        ratio2 = float(overlap)/length2

        return max(ratio1, ratio2)


myfasta = open('36.36_loci_v2.fa', 'r')

fastadict = dict()

for line in myfasta:
	fastadict[line.strip()[1:]] = next(myfasta).strip()

myfasta.close()

out = open('36.36.new_loci_v2.fa', 'w')

myblast = open('36.36.blastoutput', 'r')

alreadyseen = []

badlist = []

for line in myblast:
	info = line.strip().split('\t')

	if info[1] in alreadyseen:
		badlist.append(info[1])
	else:
		alreadyseen.append(info[1])

myblast.close()

myblast = open('36.36.blastoutput', 'r')


alreadyseen = []

for line in myblast:
	info = line.strip().split('\t')
	if info[1] in badlist:
		continue
	else:
		

		if info[0] in alreadyseen:
			a = [start, end]
			b = [int(info[6]), int(info[7])]
			print line
			print checkoverlap(a,b)
			if checkoverlap(a,b) > .2:
				print line			


		alreadyseen.append(info[0])

		start = int(info[6])
		end = int(info[7])

		out.write('>' + '|'.join(info[1].split('|')[0:5]) +'|' + info[0] + '\n')
		out.write(fastadict[info[1]] + '\n')















