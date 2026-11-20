from math import *
from sys import stdin
	
#===KhanhVyB25DCTC140===	
tests = int(input().strip())
while tests > 0:
	s1 = input().strip()
	s2 = s1[::-1]
	
	ok = True
	for i in range(1, len(s1)):
		if abs(ord(s1[i]) - ord(s1[i - 1])) != abs(ord(s2[i]) - ord(s2[i - 1])):
			ok = False
			break
			
	if(ok):
		print("YES")
	else:
		print("NO")
	
	tests -= 1