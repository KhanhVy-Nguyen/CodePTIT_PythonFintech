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


def isPrimeTotal(n):
    s = str(n)
    total = 0

    for c in s:
        c = int(c)
        total += c

    return isPrime(total)

tests = int(input())
for _ in range(tests):
    n = input().strip()

    if isPrimeTotal(n):
        print("YES")
    else:
        print("NO")