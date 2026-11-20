from math import *
from re import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

def getResult(n):
    n = int(n)
    sum = 0
    if(n % 2 == 0):
        for i in range(2, n + 1, 2):
            sum += 1 / i
    else:
        for i in range(1, n + 1, 2):
            sum += 1 / i

    return sum

tests = int(input().strip())
for _ in range(tests):
    n = int(input().strip())

    res = getResult(n)
    print(f"{res : .6f}")