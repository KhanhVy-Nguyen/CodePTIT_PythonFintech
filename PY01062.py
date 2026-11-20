from math import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

def isPrime(n):
     if n < 2: return False
     else:
          for i in range(2, isqrt(n) + 1):
               if n % i == 0:
                    return False
     return True


def isOk(s):
    s = str(s)

    digit_cnt = 0
    notPrime = 0
    Prime = 0
    for c in s:
        digit_cnt += 1
        c = int(c)

        if isPrime(c):
             Prime += 1
        else:
             notPrime += 1

    if not isPrime(digit_cnt):
     return False

    if notPrime > Prime:
     return False

    return True


tests = int(input())
for _ in range(tests):
    s = input().strip()

    if isOk(s):
        print("YES")
    else:
        print("NO")