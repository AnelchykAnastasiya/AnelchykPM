import sys
import random

n = int(sys.argv[i])

i = 0
p = 0
while i<n:
	chislo1 = random.randint(1,6)
	chislo2 = random.randint(1,6)
	if(chislo1 == 6 or chislo2 == 6):
		p = p+1
	i +=1
rez = p/n
print("%12.6f" %rez)