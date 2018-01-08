


counter = 0
while counter < 19:
	mybatch = open('mappingBatch', 'r')

	out = open('mappingbatch' + str(counter), 'w')

	for line in mybatch:
		if 'maptest' in line:
			line = line.replace('maptest', 'mapfile' + str(counter))
			out.write(line)
		else:
			out.write(line)
	out.close()
	counter += 1
