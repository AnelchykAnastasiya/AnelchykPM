import sys
import math

try:
	outfilename = sys.argv[1]
except:
	print ("Usage:", sys.argv[0], "infile outfile")
	sys.exit(1)
ofile = open(outfilename, 'w')
def myfunc(y):
    if y >= 0.0:
        return y**5*math.exp(-y)
    else:
        return 0.0