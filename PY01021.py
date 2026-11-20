from math import *
from sys import stdin
	
#===KhanhVyB25DCTC140===	
tests = int(input())
while tests > 0:
	s = input().strip()
	
	letters = []
	total = 0
	
	for c in s:
		if c.isalpha():
			letters.append(c)
		elif c.isdigit():
			total += int(c)
	
	letters.sort()
	res = "".join(letters) + str(total)
	
	print(res)
	
	tests -= 1