from math import *

	
#===KhanhVy_B25DCTC140===

def isPrime(n):
	if n < 2:
		return False
	lim = isqrt(n)
	for i in range(2, lim + 1):
		if n % i == 0:
			return False
	return True
	
	
t = int(input().strip())
while t > 0:
	n = int(input().strip())
	k = 0
	
	for i in range(1, n):
		if gcd(i, n) == 1:
			k += 1
	
	if isPrime(k):
		print("YES")
	else:
		print("NO")
	t -= 1