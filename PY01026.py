from math import *
from sys import stdin

#===NNKhanhVyB25DCTC140===
def ok(s1, s2 ):
    for x in s1:
        if s1.count(x) != s2.count(x):
            return False
    return True
tests = int(input())
for t in range (1, tests + 1):
    s1 = input().strip()
    s2 = input().strip()

    if ok(s1, s2):
        print("Test " + str(t) + ": YES")
    else:
        print("Test " + str(t) + ": NO")