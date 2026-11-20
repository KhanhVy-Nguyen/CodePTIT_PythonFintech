from math import *
from re import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

def isDi(n):
    s = str(n)
    sum = 0
    for c in s:
        c = int(c)
        sum += c

    return sum % 3 == 0

tests = int(input())
for _ in range(tests):
    s = input().strip()

    if isDi(s):
        print("YES")
    else:
        print("NO")