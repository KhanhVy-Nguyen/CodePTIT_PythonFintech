from math import *
import sys
	
#===KhanhVyB25DCTC140===	
#rv
t = int(input())

for _ in range(t):
    n = int(input())
    parts = ["1"]
    d = 2
    while d * d <= n:
        if n % d == 0:
            count = 0
            while n % d == 0:
                count += 1
                n //= d
            parts.append(f"{d}^{count}")
        d += 1
    if n > 1:
        parts.append(f"{n}^1")

    print(" * ".join(parts))
