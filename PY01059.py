from math import *
from re import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

def getEvenTotal(s):
    s = str(s)
    sum = 0
    for i in range(0, len(s), 2):
        sum += int(s[i])

    return sum

def getOddMulti(s):
   multi = 1
   hasNoneZero = False

   for i in range(1, len(s), 2):
       if s[i] != "0":
            multi *= int(s[i])
            hasNoneZero = True

   if hasNoneZero == False:
       multi = 0

   return multi
           

tests = int(input())
for _ in range(tests):
    n = input().strip()

    total = getEvenTotal(n)
    multi = getOddMulti(n)

    print(total, multi)