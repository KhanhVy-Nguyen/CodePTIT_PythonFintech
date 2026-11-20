from math import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



tests = int(input())
for _ in range(tests):
    s = map(int, input().split())
    n, k = s

    list = []
    for i in range(n - 1):
        s1 = "".join(list)
        list.append(s1)
        list.append(alpha[i])
        list.append(s1)

    print(list)
    res = "".join(list)
    print(res)

