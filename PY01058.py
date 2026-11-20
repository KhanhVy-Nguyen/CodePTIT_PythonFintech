from math import *
from re import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

def isPrime(n):
    n = int(n)
    if n < 2 :
        return False
    else:
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
    return True

tests = int(input())
for _ in range(tests):
    s = input().strip()
    check = int(s[-4:])

    if isPrime(check):
        print("YES")
    else:
        print("NO")