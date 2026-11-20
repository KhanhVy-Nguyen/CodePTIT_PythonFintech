from math import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

s = map(int, input().split())
n , k = s

cnt = 0
start = 10 ** (k - 1)
end = 10 ** (k)
for i in range( start, end ):
    if gcd(i, n) == 1:
        if cnt == 10:
            print()
            cnt = 0
        print(i, end = " ")
        cnt += 1