from math import *
from re import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

def isOk(s):
    s = str(s)
    if len(s) < 3:
         return False
    
    first = s[:len(s) - 3]
    last = s[-3:]
    for i in range(1, len(last)):
        if int(s[i - 1]) - int(s[i]) <= 0:
            return False

    #for i in range(1, len(first)):

    