def getTotalDigits(n):
    n = str(n)
    total = 0
    for c in n:
        c = int(c)
        total += c
    return total

tests = int(input())
for _ in range(tests):
    n = int(input())
    sn = list(map(int, input().split()))

    sn.sort(key = lambda x: (getTotalDigits(x), x))
    print(*sn)


