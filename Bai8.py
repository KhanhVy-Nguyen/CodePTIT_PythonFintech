def isPrime(n):
    if n < 2 : 
        return False
    else:
        for i in range (2, int(n **0.5) + 1):
            if n % i == 0:
                return False
        return True



t = int(input())
a = list(map(int, input().split()))
freq = {}
order = []

for x in a :
    if isPrime(x):
        if x not in freq:
            freq[x] = 0
            order.append(x)
        freq[x] += 1

for x in order:
    print(x, freq[x], end = " ")
    print()
