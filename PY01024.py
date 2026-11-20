from math import *
from sys import stdin
	
#===KhanhVyB25DCTC140===	
	
tests = int(input())
while tests > 0:
	s = input().strip()
	total = 0
	ok = True
	for i in range(1, len(s)):
		if abs(int(s[i]) - int(s[i - 1]))!= 2:
			ok = False
		total += int(s[i - 1])

	total += int(s[-1:])
	
	if total % 10 != 0:
		ok = False
	
	
	if(ok):
		print("YES")
	else:
		print("NO")
	
	
	tests -= 1