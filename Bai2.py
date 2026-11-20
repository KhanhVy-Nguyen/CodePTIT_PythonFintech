def isTotalTen(n):
    total = sum(int(x) for x in str(n))
    return total % 10 == 0

def isTwoDigits(s):
    s = str(s)
    length = len(str(s))
    for i in range(1, length):
        if(abs(int(s[i]) - int(s[i - 1])) != 2):
            return False
    return True

tests = int(input().strip())
for _ in range(tests):
    n = input().strip()
    if isTotalTen(n) and isTwoDigits(n):
        print("YES")
    else:
        print("NO")
    