import random
import sys 

n = int(sys.argv[1])
i = 0
s = 0
while i < n:
	r = random.uniform(-1,1)
	print("%.4f" % r)
	s = s+r
	i = i+1
s = s/n
print("%.4f" % s)