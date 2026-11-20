from math import *
from sys import stdin
	
#===KhanhVyB25DCTC140===	

s = map(int, stdin.read().strip().split())
a, k, n = s

first_sum = ((a // k) + 1) * k
first_b = first_sum - a
max_b = n - a

if first_b > max_b:
	print(-1)
else:
	print(*(range(first_b, max_b + 1, k)))