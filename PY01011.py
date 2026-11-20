from math import *

	
#===KhanhVy_B25DCTC140===	
def isPalindrome(s):
	s = str(s)
	
	if len(s) % 2 != 0: return False
	
	if s != s[::-1]: return False
	
	for c in s:
		if c not in '02468':
			return False
	
	return True

tests = int(input().strip())
# while tests > 0:
# 	n = int(input().strip())
# 	for i in range(n):
# 		if isPalindrome(i):
# 			print(i, end = " ")
	
		
# 	print()
# 	tests -= 1

for i in range (tests):
	n = int(input().strip())
	for i in range(n):
		if isPalindrome(i):
			print(i, end = " ")
	print()