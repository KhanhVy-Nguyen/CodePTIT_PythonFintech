from math import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

def isOk(n):
    n = str(n)

    c1 = n[0]
    c2 = n[1]

    for i in range (2, len(n)):
        if i % 2 == 0 and c1 != n[i]:
            return False
        elif i % 2 != 0 and c2 != n[i]:
            return False
    return True

tests = int(input())
for _ in range(tests):
    s = input().strip()

    if isOk(s):
        print("YES")
    else:
        print("NO")