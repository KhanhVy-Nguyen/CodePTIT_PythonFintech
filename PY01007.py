from math import *

	
#===KhanhVy_B25DCTC140===	
tests = int(input().strip())
while tests > 0:
	s = map(float, input().strip().split())
	Deposit, InterestRate, Target = s
	
	y = 0
	while Deposit <= Target:
		Deposit = Deposit + Deposit * InterestRate / 100
		y += 1
	print(y)
	
	tests -= 1