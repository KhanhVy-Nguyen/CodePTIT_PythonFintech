from math import *

	
#===KhanhVy_B25DCTC140===	
s = input().strip()
cap_cnt = 0
small_cnt = 0

for c in s:
	if c.isupper(): cap_cnt += 1
	elif c.islower(): small_cnt += 1

if small_cnt >= cap_cnt:
	s = s.lower()
elif cap_cnt > small_cnt:
	s = s.upper()

print(s)
		