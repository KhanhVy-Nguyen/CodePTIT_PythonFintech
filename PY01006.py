from math import *

	
#===KhanhVy_B25DCTC140===	

tests = int(input().strip())
while tests > 0:
	ok = True
	num = input().strip()
	for c in num:
		if "47".find(c) == -1:
			ok = False
			break
	
	if(ok): 
		print("YES")
	else:
		print("NO")
	tests -= 1