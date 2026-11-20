from math import *
from sys import stdin
	
#===KhanhVyB25DCTC140===	
P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
	line = input().strip().split()
	if line[0] == "0": break
	
	k = int(line[0])
	s = str(line[1])
	
	encoded = []
	
	for c in s:
		idx = P.index(c)
		new = P[(idx + k) % 28]
		encoded.append(new)
	
	res = "".join(reversed(encoded))
	print(res)
	
	