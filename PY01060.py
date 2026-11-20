from math import *
from re import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

def getEvenMulti(n):
    s = str(n)
    multi = 1
    for i in range(0, len(s), 2):
        if s[i] != '0':
            multi *= int(s[i])
    return multi

def getOddSum(n):
    s = str(n)
    sum = 0
    for i in range(1, len(s), 2):
        sum += int(s[i])
    return sum 

tests = int(input())
for _ in range(tests):
    n = input().strip()

    Multi = getEvenMulti(n)
    Sum = getOddSum(n)

    print(Multi, Sum)