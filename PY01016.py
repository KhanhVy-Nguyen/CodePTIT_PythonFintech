from math import *

	
#===KhanhVyB25DCTC140===	
tests = int(input().strip())
while tests > 0:
	s = input().strip()
	power = 0
	for i in range(len(s)):
		if i % 2 == 0:
			al = s[i]
		elif i % 2 != 0:
			power = int(s[i])
			
			for j in range(power):
				print(al, end = "")
		
	print()
	
	tests -= 1
