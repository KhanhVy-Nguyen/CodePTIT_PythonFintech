from math import *

	
#===KhanhVy_B25DCTC140===	
def isPrime(n):
	if n < 2: return False
	lim = isqrt(n)
	for i in range(2, lim + 1):
		if n % i == 0: return False
	return True

def sum (n):
	sum = 0
	while n > 0:
		sum += n % 10
		n //= 10
	return sum
	
tests = int(input().strip())
while tests > 0:
	m = map(int, input().strip().split())
	a, b = m
	common = gcd(a, b)
	total = sum(common)
	
	if isPrime(total):
		print("YES")
	else:
		print("NO")
	tests -= 1