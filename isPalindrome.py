def isPalindrome(n):
    n = str(n)
    rev = n[::-1]
    return n == rev

n = input()
if isPalindrome(n):
    print("YES")
else:
    print("NO")