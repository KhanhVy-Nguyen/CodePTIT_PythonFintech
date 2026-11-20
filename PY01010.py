from math import *

	
#===KhanhVy_B25DCTC140===	
tests = int(input().strip())
while tests > 0:
	s = input().strip()
	first = s[:2]
	last = s[-2:]
	
	if first == last:
		print("YES")
	else:
		print("NO")
	
	tests -= 1