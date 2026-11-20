n = int(input())
a = []
while len(a) < n:
    a.extend(map(int, input().split()))
evens = sorted([x for x in a if x % 2 == 0])
odds = sorted([x for x in a if x % 2 != 0], reverse=True)

e_idx = 0
o_idx = 0
res = []

for x in a:
    if x % 2 == 0:
        res.append(str(evens[e_idx]))
        e_idx += 1
    else:
        res.append(str(odds[o_idx]))
        o_idx += 1

print(*(res))
