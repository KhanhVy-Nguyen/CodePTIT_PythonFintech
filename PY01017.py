from math import *
from sys import stdin
	
#===KhanhVyB25DCTC140===	
tests = int(input().strip())
while tests > 0:
	s = input().strip()
	encoded = []
	power = 0
	cnt = 1
	for i in range(len(s) - 1):
		if s[i] == s[i + 1]:
			cnt += 1
		else:
			encoded.append(f"{cnt}{s[i]}")
			cnt = 1
			
	encoded.append(f"{cnt}{s[-1]}")
	res = "".join(encoded)
	print(res)
	tests -= 1
	