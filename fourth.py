import sys
import math

def logarithm(n):
	if float(n)<0:
		print('ln('+"%d" %(float(n))+') is illegal')
	else:
		print('ln('+"%d" %(float(n))+') = ' "%g" %(math.log(float(n))))

logarithm(sys.argv[1])