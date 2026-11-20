from math import *
from re import *
from sys import stdin

#===NNKhanhVyB25DCTC140===

"""
Trong hệ cơ số thập phân, một số được gọi là thuận nghịch nếu đọc ngược lại ta vẫn thu được chính số đó. 
Ví dụ: 12321, 2345432, 111111 …

Chúng ta mở rộng khái niệm như sau: cho hệ cơ số K, giá trị thập phân x được gọi là thuận nghịch
 trong cơ số K nếu biểu diễn của x trong cơ số K có giá trị giống nhau khi viết xuôi và khi viết ngược. 
 Với giả thiết biểu diễn trong hệ cơ số K bất kỳ (2 ≤ K ≤ 100000) là cách sử dụng chính các giá trị số từ 0 
 đến K-1 chứ không dùng các chữ cái.

Bài toán đặt ra là cho đoạn [a,b] và số M. Hãy đếm các số trong đoạn [a,b] là thuận nghịch trong tất cả các cơ số 2 ≤ K ≤ M.
"""
"""
def isPalindrome(x, k):
    li = []
    while x > 0:
        li.append(x % k)
        x = x // k
    return li == li[::-1]                //these blocks dont work, got TLE in CodePTIT
                                         //coded by myself

a, b, m = map(int, input().split())

cnt = 0
for x in range(a, b + 1):
    ok = True
    lim = min(m, x)
    for k in range(2, lim + 1):
        if not isPalindrome(x, k):
            ok = False
            break
    if ok:
        cnt += 1

print (cnt)
"""

# AI
a, b, m = map(int, input().split())
if m >= 4:
    cnt = 0
    if a <= 0 <= b:
        cnt += 1
    if a <= 1 <= b:
        cnt += 1
    print(cnt)
else:
    pals = [0]
    for i in range(1, 2048):
        s = bin(i)[2:]
        p1 = int(s + s[::-1], 2)
        p2 = int(s + s[:-1][::-1], 2)
        if p1 <= 2000000:
            pals.append(p1)
        if p2 <= 2000000:
            pals.append(p2)
            
    cnt = 0
    for x in pals:
        if a <= x <= b:
            if m == 2:
                cnt += 1
            else:
                li = []
                temp = x
                while temp > 0:
                    li.append(temp % 3)
                    temp //= 3
                if li == li[::-1]:
                    cnt += 1
    print(cnt)

#darkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk