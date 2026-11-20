s = input().strip()
d = {}
n = len(s)
if n % 2 != 0:
    n -= 1

for i in range(0, n, 2):
    num = int(s[i:i + 2])
    if num not in d:
        d[num] = 1
    else:
        d[num] += 1

for num in d:
    print(num, d[num])