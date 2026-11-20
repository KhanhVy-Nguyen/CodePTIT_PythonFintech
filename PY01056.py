from math import *
from re import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

def isPrime(n):
    n = int(n)
    if n < 2 :
        return False
    else:
        for i in range(2, isqrt(n)):
            if n % i == 0:
                return False
    return True

def isOk(n):
    s = str(n)
    sum = 0

    for i in range(len(s)):
        sum += int(s[i])
        if not (i % 2 == 0 or int(s[i]) % 2 != 0):
            return False
        elif not (i % 2 != 0 or int(s[i]) % 2 == 0):
            return False
    
    if not isPrime(sum):
        return False

    return True

tests = int(input())
for _ in range(tests):
    s = input().strip()

    if isOk(s):
        print("YES")
    else:
        print("NO")