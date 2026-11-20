from math import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

tests = int(input())
for _ in range(tests):
    s = input().strip()
    n = input().strip()

    print(s.count(n), end = "\n")