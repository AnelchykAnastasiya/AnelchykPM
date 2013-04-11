import sys
import math

def logarithm(n):
	if float(n)<0:
		print('ln('+"%d" %(float(n))+') is illegal')
	else:
		print('ln('+"%d" %(float(n))+') = ' "%g" %(math.log(float(n))))

for r in sys.argv[1:]:
	logarithm(r)

for i in range(1,len(sys.argv)):
	logarithm(sys.argv[i])

j = 1
while j<len(sys.argv):
	logarithm(sys.argv[j])
	j +=1
