from math import *
from re import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

def isAlternate(n):
    n = str(n)

    if len(n) % 2 == 0:
        return False

    if n[0] == n[1]:
        return False

    for i in range(2, len(n) + 1, 2):
        if n[i - 2] != n[i]:
            return False

    return True

tests = int(input())
for _ in range(tests):
    n = input().strip()

    if isAlternate(n):
        print("YES")
    else:
        print("NO")