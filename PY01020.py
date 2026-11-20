from math import *
from sys import stdin
	
#===KhanhVyB25DCTC140===	
tests = int(input())
while tests > 0:
	s = input().strip()
	
	if s[-2:] == "86":
		print("YES")
	else:
		print("NO")
		
	tests -= 1