nums = []
while len(nums) < 10:
   nums.extend(map(int, input().split()))

remainders = set(x % 42 for x in nums)
print(len(remainders))