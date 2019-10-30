n = int(input())
nums = [int(x) for x in input().split()]

for i in range(n):
    nums[i] = (n + 1) - nums[i]

print(*nums)
