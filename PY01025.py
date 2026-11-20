from math import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

n = input().strip()
cnt = 0

list = []
for x in reversed(n):
   if cnt == 3:
      list.append(",")
      cnt = 0
   list.append(x)
   cnt += 1
   
res = "".join(reversed(list))

print(res)