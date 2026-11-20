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

def isOk(s):
    s = str(s)
    ex = "2357"

    for i in range(len(s)):
        
        if isPrime(i):
            if s[i] not in ex:
                return False
        else:
            if s[i] in ex:
                return False
            
    return True

tests = int(input())
for _ in range(tests):
    n = input().strip()

    if isOk(n):
        print("YES")
    else:
        print("NO")