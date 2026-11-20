from math import *

	
#===KhanhVy_B25DCTC140===	
s1 = input().strip()
s2 = input().strip()
index = int(input().strip()) - 1
res = s1[:index] + s2 + s1[index:]
print(res)