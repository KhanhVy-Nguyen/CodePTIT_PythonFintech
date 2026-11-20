from math import *

	
#===KhanhVyB25DCTC140===	
def isNotDe(s):
	s = str(s)
	
	for i in range(1, len(s)):
		if s[i] < s[i - 1]: 
			return False
	
	return True
	
tests = int(input().strip())
while tests > 0:
	s = input().strip()
	if(isNotDe(s)):
		print("YES")
	else:
		print("NO")
	tests -= 1