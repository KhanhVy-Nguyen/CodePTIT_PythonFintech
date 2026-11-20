from math import *
from re import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

def isPrime(n):
    n = int(n)
    if n < 2: 
        return False
    else:
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
    return True

n, m = map(int, input().split())

matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    for i in range(m):
        if isPrime(row[i]):
            row[i] = 1
        else:
            row[i] = 0
    matrix.append(row)


for i in range(n):
    for j in range(m):
        print(matrix[i][j], end = " ")
    print()


