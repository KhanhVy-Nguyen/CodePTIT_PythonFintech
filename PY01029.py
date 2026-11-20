from math import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

def getPalin(n):
    a = 0
    while n > 0:
        a = a * 10 + n % 10
        n //= 10

    return a 


tests = int(input())
for _ in range(tests):
    n = int(input())
    rev = getPalin(n)

    if gcd(n, rev) == 1:
        print("YES")
    else:
        print("NO")