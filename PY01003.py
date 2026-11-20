from math import *

	
#===KhanhVy_B25DCTC140===
tests = int(input())
while tests > 0:
	n = int(input().strip())
	p = 10
	while n > p:
		n = ((n + p // 2) // p) * p
		p *= 10
	print(n)
	tests -= 1