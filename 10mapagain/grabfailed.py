import os
import sys


myfile = open('myerrors', 'r')

out = open('failedsamples', 'w')

alreadyseen = []

for line in myfile:
	if "2trim" in line:
		myID =line.strip().split('2trim/')[1].split('.final')[0]

		if myID in alreadyseen:
			continue
		else:
			out.write(myID + '\n')
			alreadyseen.append(myID)


	elif '9blastagain' in line:
                myID =line.strip().split('9blastagain/')[1].split('_phylo')[0]

                if myID in alreadyseen:
                        continue
                else:
                        out.write(myID+'\n')
                        alreadyseen.append(myID)

