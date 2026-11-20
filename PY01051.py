from math import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

def isPalindrome(n):
    n = str(n)
    if len(n) <= 1: 
        return False
    
    rev = n[::-1]

    return n == rev

def isPalinTotal(n):
    n = str(n)
    total = 0
    for c in n:
        c = int(c)
        total += c
    return isPalindrome(str(total))

tests = int(input())
for _ in range (tests):
    s = input().strip()

    if isPalinTotal(s):
        print("YES")
    else:
        print("NO")

