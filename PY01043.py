from math import *
from re import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

def isOk(s):
    s = str(s)

    if s != s[::-1]:
        return False

    if len(s) % 2 != 0:
        return False
    
    for i in s:
        i = int(i)
        if i % 2 != 0:
            return False

    return True

tests = int(input().strip())
for _ in range (tests):
    n = int(input().strip())

    for i in range (n):
        if isOk(i):
            print(i, end = " ")
    print()
    