from math import *
from re import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

def isBalance(s):
    s = str(s)
    rev = s[::-1]

    lim = len(s) // 2 + 1

    for i in range(1, lim):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(rev[i]) - ord(rev[i - 1])):
            return False

    return True

tests = int(input())
for _ in range(tests):
    s = input().strip()

    if isBalance(s):
        print("YES")
    else:
        print("NO")

