tests = input()

s1 = sorted(set(map(int, input().split())))
s2 = sorted(set(map(int, input().split())))

for c in s1:
    if c in s2:
        print(c, end = " ")
print()

for c in s1:  
    if c not in s2:
        print(c, end = " ")
print()

for x in s2:
    if x not in s1:
        print(x, end = " ")