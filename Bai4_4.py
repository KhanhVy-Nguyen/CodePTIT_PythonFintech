import re

n, k = map(int, input().split())
d = {}
for _ in range(n):
    s = input().lower()
    ws = re.findall(r'[a-z0-9]+', s)

    for w in ws:
        if w not in d:
            d[w] = 1
        else:
            d[w] += 1

res = []
for w in d:
    if d[w] >= k:
        res.append(w)

res.sort(key = lambda w: (-d[w], w))

for w in res:
    print(w, d[w])

    