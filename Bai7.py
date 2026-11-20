from collections import Counter

tests = int(input())
for _ in range(tests):
    n = int(input())
    a = list(map(int, input().split()))

    cnts= Counter(a)
    ans = None
    for num, cnt in cnts.items():
        if cnt > n // 2:
            ans = num
            break

    if ans is not None:
        print(ans)
    else:
        print("NO")