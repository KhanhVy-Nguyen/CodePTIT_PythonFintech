from math import *
from re import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

n = input().strip()
if(fullmatch(r'(688|68|6)+', n)):
    print("YES")
else:
    print("NO")