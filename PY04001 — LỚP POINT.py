from math import *
from re import *
from sys import stdin
from decimal import Decimal

#===NNKhanhVyB25DCTC140===

class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def distance(self, another):
        res = sqrt((self.x - another.x) ** 2 + (self.y - another.y) ** 2)
        return f"{res:.4f}"


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1