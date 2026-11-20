while True:
    n = int(input())
    if n == 0:
        break

    a = [int(input()) for _ in range(n)]

    min_val = min(a)
    max_val = max(a)

    if min_val == max_val:
        print("BANG NHAU")
    else:   
        print(min_val, max_val)