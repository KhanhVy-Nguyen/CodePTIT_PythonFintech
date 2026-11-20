from math import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

def getMulti(s):
    s = str(s)

    res = 1

    for x in s:
        x = int(x)
        if x != 0:
            res *= x

    return res

tests = int(input())
for _ in range(tests):
    s = input().strip()

    res = getMulti(s)
    print(res)