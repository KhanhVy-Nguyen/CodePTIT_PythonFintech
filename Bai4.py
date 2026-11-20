tests = int(input().strip())
while tests > 0:
    n = input().strip()
    total = 0
    for x in n:
        total += int(x)
    tests -= 1
    if total % 3 == 0:
        print("YES")
    else:
        print("NO")