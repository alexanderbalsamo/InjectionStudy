# Run on a public html page of PyGRB Output
# start in GRB190420981_100NSNS-100NSBH_CLOSED
# and to run:
# python exDistErrors.py XXXXX_FILTERED_30

import math
import os
import sys	
import numpy as np

# Lists
errors_90 = []
errors_50 = []

def fileErrors(fileName):
	# Open file
	file = open(fileName, "rt")
	
	row = 0
	
	for l in range(3):
		line=file.readline()
	
	past90 = False
	while(line):
		data = line.strip().split("\t")
		if float(data[1]) < 9.0e-01 and not past90:
			sigma90 = error(pLine, data, 90)
			errors_90.append(sigma90)
			past90 = True

		if float(data[1]) < 5.0e-01:
			sigma50 = error(pLine, data, 50)
			errors_50.append(sigma50)
			break

		# Look to next row	
		pLine = data
		row = row + 1
		line = file.readline()
	
	file.close()

def error(pData, data, p):
	preD = float(pData[0])
	d = float(data[0])
	preE = float(pData[1])
	e = float(data[1])
	sigPreE = (float(pData[2])+float(pData[3]))/2.
	sigE = (float(data[2])+float(data[3]))/2.

	partialE = ((preD-d)*(100*preE-p))/(100*(preE-e)**2)
	partialPreE = ((d-preD)*(e-p/100.))/(preE-e)**2

	sigma = math.sqrt(partialE**2*sigE**2 + partialPreE**2*sigPreE**2)
	return sigma

# Do the thing
generalDirectoryName = "efficiency_OFFTRIAL_1"
top = sys.argv[1]
for i in range(6):
	for root, dirs, files in os.walk(top + "/" + generalDirectoryName):
	    for name in files:
	        if name.endswith("efficiency_numbers.txt"):
	            fileErrors(top + "/" + generalDirectoryName + "/" + name)
	generalDirectoryName = generalDirectoryName[:-1]+str(i+2)

print("90% Error: " + str(np.mean(errors_90)))
print("50% Error: " + str(np.mean(errors_50)))