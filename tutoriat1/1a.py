from math import ceil

n, m, a = input().split()
n, m, a = int(n), int(m), int(a)

width = ceil(n / a)
height = ceil(m / a)

print(width * height)
