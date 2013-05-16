import sys
import math

try:
	infilename = sys.argv[1]
	outfilename = sys.argv[2]

except:
	print ("Usage:", sys.argv[0], "infile outfie")
	sys.exit(1)
ifile = open(infilename,'r')
ofile = open(outfilename, 'w')

def ser(s):
	i = 0
	sum = 0
	while i < len(s):
		sum += float(s[i])
		i += 1
	rez = sum/len(s)
	return rez

	

for line in ifile.readlines():
	str1 = line.split()
	i = 0
	while i<len(str1):
		ofile.write("%12.6f" %(float(str1[i])))
		ofile.write(' ')
		i+=1
	ofile.write("%12.6f" %(float(ser(str1))))
	ofile.write('\n')

ofile.close()
ifile.close()