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
i=2
while i < len(sys.argv):
    x = float(sys.argv[i])
    i+=1
    fy = myfunc(float(sys.argv[i]))
    ofile.write((str(x)+' '+str(fy)+'\n'))
    i+=1
ofile.close()