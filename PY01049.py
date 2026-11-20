from math import *
from re import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

def isPrime(n):
    n = int(n)

    if n < 2:
        return False
    else:
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
    return True

def isOk(n):
    s = str(n)

    if not isPrime(len(s)):
        return False

    P = 0
    nP = 0

    for c in s:
        c = int(c)
        if isPrime(c):
            P += 1
        else:
            nP += 1

    if P <= nP:
        return False

    return True
    

tests = int(input())
for _ in range(tests):
    n = input().strip()

    if isOk(n):
        print("YES")
    else:
        print("NO")