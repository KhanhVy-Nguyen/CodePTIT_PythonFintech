from math import *
from re import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

def isPrime(n):
    n = int(n)

    if n < 2: 
        return False
    else:
        for i in range(2, isqrt(n)):
            if n % i == 0:
                return False

    return True

tests = int(input())
for _ in range(tests):
    n = input().strip()

    first = n[:3]
    last = n[-3:]

    if isPrime(first) and isPrime(last):
        print("YES")
    else:
        print("NO")

# s = "abcxyz"
# print(s[:3], s[-3:])