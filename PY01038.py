from math import *
from re import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

def getPalindrome(n):
    n = str(n)
    return n[::-1]

tests = int(input().strip())
for _ in range(tests):
    sum = int(input().strip())
    cnt = 0
    while sum % 7 != 0:
        cnt += 1
        if cnt == 1000:
            print("-1")
            break

        sum += int(getPalindrome(sum))

    print(sum)

